from django.urls import path
from . import views

urlpatterns = [
    path('', views.SLS_home, name='StreetLeagueSkateboarding_home'),
]