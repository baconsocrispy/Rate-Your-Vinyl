from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cars,name='Carhome'),
    path('CarsCreate', views.Cars,name='CarCreate'),

]