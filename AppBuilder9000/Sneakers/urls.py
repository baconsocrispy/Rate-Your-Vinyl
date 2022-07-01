from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sneakers_home, name="Sneakers_home")
]