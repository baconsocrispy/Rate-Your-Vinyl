from . import views
from django.urls import path

urlpatterns = [
    path('', views.SuperCarsHome, name='SuperCars_Home'),

]