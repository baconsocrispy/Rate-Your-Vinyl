from django.urls import path

from . import views

urlpatterns = [
    path('', views.SportsCars_Home, name='SportsCars_Home'),

]