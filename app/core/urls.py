from django.urls import path

from .views import HomeView, UserSettingsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]