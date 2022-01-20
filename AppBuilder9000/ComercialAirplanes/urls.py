from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='ComercialAirplanes_home'),
    path('addpage', views.addpage, name='ComercialAirplanes_add'),
    path('Collection', views.Collection, name='CommercialAirplanes/CommercialAirplanes_Collection.html')
]