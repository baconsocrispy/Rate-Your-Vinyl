from . import views
from django.urls import path

urlpatterns = [
    path('', views.Super_Cars_Home, name='SuperCars_Home'),

]