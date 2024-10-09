from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('', include('login.urls')),
    path('', include('gallery.urls')),
    path('', include('cats.urls')),
    path('admin/', admin.site.urls),
]
