from django.urls import path
from . import views

urlpatterns = [
    path('', views.MagicTheGathering_home, name='MagicTheGathering_home'),
    path('create/', views.create_collection, name='create'),
    path('add/', views.create_card, name='add'),
    ]