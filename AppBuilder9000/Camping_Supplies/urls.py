from django.urls import path
from . import views

urlpatterns = [
    path('', views.Camping_Supplies_Home, name='Camping_Supplies_Home'),
]