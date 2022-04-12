from django.urls import path
from . import views
from django.contrib import admin

urlpatters = [
    path('', views.Muay_Thai_Home, name='Muay_Thai_Home'),

]

