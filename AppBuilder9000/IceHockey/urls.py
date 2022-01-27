
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IceHockey_home, name='IceHockey_home'),
    path('newprofile', views.IceHockey_newprofile, name='IceHockey_newprofile'),
    path('myprofile', views.IceHockey_myprofile, name='IceHockey_myprofile'),
]