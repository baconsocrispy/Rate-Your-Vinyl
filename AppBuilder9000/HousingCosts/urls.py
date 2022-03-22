from django.urls import path
from . import views

urlpatterns = [
    path('', views.housing_costs_home, name='housing_costs_home'),
]