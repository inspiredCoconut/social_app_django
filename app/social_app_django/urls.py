from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('posts.urls')),
    path('', include('management.urls')),
    path('', include('saves.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
    path('', include('shares.urls')),
    path('', include('comments.urls')),
]