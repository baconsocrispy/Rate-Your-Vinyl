from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_home, name='home'),
]





