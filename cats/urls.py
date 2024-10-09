from django.urls import path
from . import views

urlpatterns = [
    path('cat/', views.cats_view),
    path('api/cats/random', views.random_cat_image),
    path('api/cats/random/<int:num>', views.random_cat_images),
]
