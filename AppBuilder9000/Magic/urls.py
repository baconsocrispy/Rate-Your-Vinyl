from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.magic_home, name='magic_home'),
    path('create/', views.magic_create, name='magic_create'),
    path('browse/', views.magic_browse, name='magic_browse'),
]