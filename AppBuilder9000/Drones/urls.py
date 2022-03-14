from django.urls import path
from . import views

urlpatterns = [

    path('', views.Drones_home, name='Drones_home'),
    path('create/', views.Drones_create, name='Drones_create'),
    path('list/', views.Drones_list, name='Drones_list'),
    path('details/', views.Drones_details, name='Drones_details'),
]

# line 9 should be: path('<int:pk>/details/', views.Drones_details, name='Drones_details'),