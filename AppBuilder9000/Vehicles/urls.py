from django.urls import path
from .import views
# Url patterns for the paths of every html file to be used to link together #
urlpatterns = [
    path('', views.vehiclesHome, name='Vehicles_home'),
    path('addVehicles/', views.addVehicles, name='Vehicles_add'),
    path('/vehicles', views.vehicles_view, name='Vehicles_view'),
]