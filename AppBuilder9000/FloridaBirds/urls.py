from django.urls import path
from .import views

urlpatterns = [
    path('', views.florida_birds_home, name='florida_birds_home'),
    path('add-bird/', views.add_bird, name='florida_birds_add_bird'),
]