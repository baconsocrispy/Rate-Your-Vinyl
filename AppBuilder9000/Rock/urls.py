
from django.urls import path
from . import views

urlpatterns = [
    path('RocksHome', views.RocksHome, name='RocksHome'),
    path('Rock_Create', views.Rock_Create, name='Rock_Create'),


]