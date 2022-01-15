from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='ComercialAirplane_home'),
    path('', views.addpage, name="addplane"),
]