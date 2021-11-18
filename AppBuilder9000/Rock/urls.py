from django.urls import path
from . import views

urlpatterns = [
    path('', views.RocksHome, name='RocksHome'),

]