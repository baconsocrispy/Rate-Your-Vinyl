from django.urls import path
from . import views

urlpatterns = [
    path('', views.housing_costs_home, name='housing_costs_home'),
    path('Create/', views.housing_costs_create, name='housing_costs_create'),
    path('List/', views.housing_costs_list, name='housing_costs_list'),
]
