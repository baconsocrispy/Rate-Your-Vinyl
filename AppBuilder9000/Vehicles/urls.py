from django.urls import path
from .import views
# Url patterns for the paths of every html file to be used to link together #
urlpatterns = [
    path('', views.vehiclesHome, name='Vehicles_home')

]