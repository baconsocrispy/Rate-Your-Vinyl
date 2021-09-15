from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cars,name='Carhome'),
    path('CarsCreate', views.CarCreate,name='CarCreate'),
    path('CarEntries', views.CarsEntries,name='CarsEntries'),
    path('CarDetails', views.CarsDetails,name='Cars Details'),

]