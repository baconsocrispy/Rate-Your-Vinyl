from django.urls import path
from . import views

urlpatterns = [
    path('', views.fe_Home, name='fe_Home'),
]
