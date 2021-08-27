from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlazerStats_Home, name='BlazerStats_Home'),
    path('Blazercreate/', views.BlazerStats_Create, name='BlazerStats_Create'),
]