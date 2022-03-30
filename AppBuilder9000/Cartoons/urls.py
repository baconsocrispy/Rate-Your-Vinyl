from django.urls import path
from . import views


urlpatterns = [
    path('', views.Cartoons, name='Cartoons_home'),
    path('create/', views.CreateCartoon, name='Cartoons_create'),
    path('list/', views.DisplayCartoons, name='Cartoons_list'),
    path('details/<int:pk>', views.DisplayDetails, name='Cartoons_details'),
]