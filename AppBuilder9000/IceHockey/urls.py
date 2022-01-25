from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ice_hockey_home'),
]