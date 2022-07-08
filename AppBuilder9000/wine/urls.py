from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

# urls which point to function in views.py

urlpatterns = [
    path('', views.wine_home, name='wine_home'),
    path('Wines/', views.wine_create, name='wine_create'),
    path('pair/', views.wine_pair, name='wine_pair'),

]
