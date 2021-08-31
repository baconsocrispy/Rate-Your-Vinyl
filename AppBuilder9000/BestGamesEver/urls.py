from django.urls import path
from . import views

urlpatterns = [
    path('', views.BestGamesEver_Home, name='BestGamesEver_Home')
]