from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.florida_birds_home, name="florida_birds_home"),
]