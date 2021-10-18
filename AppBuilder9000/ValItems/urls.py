from django.urls import path
from . import views

urlpatterns = [
    path('', views.Val_home, name='Val_home'),
    path('AddItem/', views.AddItem, name='AddItem'),
    path('Items/', views.Items, name='Items')
]
