from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketballHome, name='Basketball_Home'),
]
