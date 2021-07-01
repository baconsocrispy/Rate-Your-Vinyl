from django.urls import path
from . import views

urlpatterns = [
    path('home', views.zoo_home, name='zoo_home'),
]