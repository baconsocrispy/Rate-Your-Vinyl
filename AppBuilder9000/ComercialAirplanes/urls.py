from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='ComercialAirplane_home'),
    path('addplane', views.addpage, name="addplane"),
]