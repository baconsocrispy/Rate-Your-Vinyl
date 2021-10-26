from django.urls import path
from . import views

urlpatterns = [
       path('', views.The_Force_home, name="_Home"),
       path('Create/', views.The_Force_Create, name="TheForce"),
       path('Event/', views.The_Force_Events, name='Event'),
       path('Costumes/', views.The_Force_Costumes, name='Costumes'),
       path('Edit/', views.Edit, name='Edit'),
       path('ConfirmDelete/', views.ConfirmDelete, name='ConfirmDelete'),

]
