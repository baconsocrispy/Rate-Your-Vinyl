from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cars,name='Carhome'),
    path('CarsCreate', views.CarCreate,name='CarCreate'),
    path('CarEntries', views.CarEntries,name='CarEntries'),
    path('CarDetails', views.CarDetails,name='CarDetails'),

]