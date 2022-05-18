from django.urls import path
from . import views

urlpatterns = [
    path('', views.fe_Home, name='fe_Home'),
    path('', views.fe_Base, name='fe_Base'),
]
