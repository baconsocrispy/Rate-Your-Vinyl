from django.urls import path
from . import views

urlpatterns = [
    path('', views.marvel_home, name='marvel_home'),
    path('create/', views.marvel_create, name='marvel_create'),
]
