from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.ET_Home, name='ET_Home'),
    path('ET_Account', views.ET_Account, name='ET_Account'),
]