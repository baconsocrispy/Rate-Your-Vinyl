from django.urls import path
from . import views

urlpatterns = [
    path('', views.gardening_home, name='gardening_home'),
    path('create_plant/', views.create_plant, name="create_plant"),
    path('show_plant/', views.show_plant, name="show_plant"),
    path('<int:pk>/plant_details/', views.plant_details, name="plant_details"),
]
