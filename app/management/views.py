from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'profile_update.html'
    fields = ['first_name', 'last_name', 'email']
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile.html'
    
    def get_object(self):
        return self.request.user
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileActiveView(View):
    def get(self, request):
        user = request.user
        user.is_active = not user.is_active
        user.save()
        return redirect('profile')
    
    def post(self, request):
        user = request.user
        user.is_active = not user.is_active
        user.save()
        return redirect('profile')