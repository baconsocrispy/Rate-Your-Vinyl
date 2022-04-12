from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.Muay_Thai_Home, name='MuayThai_home'),

]

