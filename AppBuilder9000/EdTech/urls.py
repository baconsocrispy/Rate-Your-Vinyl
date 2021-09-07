from django.urls import path
from . import views

urlpatterns = [
    path('', views.EdTech_Home, name='EdTech_Home'),
]