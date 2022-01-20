from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='ComercialAirplanes_home'),
    path('addpage', views.addpage, name='ComercialAirplanes_add'),
    path('collection', views.Collection, name='ComercialAirplanes_collection')
]