from django.urls import path
from . import views

urlpatterns = [
    path('', views.Camping_Supplies_Home, name='Camping_Supplies_Home'),
    path('create/', views.Camping_Supplies_Create, name='Camping_Supplies_Create'),
]