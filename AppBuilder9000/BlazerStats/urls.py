from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlazerStats_Home, name='BlazerStats_Home'),
]