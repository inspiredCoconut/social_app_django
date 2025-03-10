from .views import LoginView, RegisterView, LogoutView, ProfileUpdateView, ProfileDetailView
from django.urls import path

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
]
