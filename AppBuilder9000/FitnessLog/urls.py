from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_home, name='fitness_home'),
    path('fitness_entry_create/', views.create_entry, name='fitness_entry_create'),
]




