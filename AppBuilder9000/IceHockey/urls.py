from django.urls import path
from . import views

urlpatterns = [
    path('', views.IceHockey_home, name='IceHockey_home'),
    path('create', views.IceHockey_create, name='IceHockey_create')
]