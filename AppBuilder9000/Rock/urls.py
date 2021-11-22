from django.urls import path
from . import views

urlpatterns = [
    path('RocksHome', views.RocksHome, name='RocksHome'),
    path('RockCreate', views.Rock_Create, name='RockCreate'),
    path('HardRock_List', views.HardRock_List, name='HardRock_List'),

]
