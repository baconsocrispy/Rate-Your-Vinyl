from django.urls import path
from .import views

urlpatterns = [
    path('', views.pokeDexHome, name='PokeDex_home'),
]