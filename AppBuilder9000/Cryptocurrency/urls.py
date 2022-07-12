from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cryptocurrency_home, name='Cryptocurrency_home'),
]
