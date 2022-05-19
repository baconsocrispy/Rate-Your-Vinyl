from django.urls import path
from . import views

urlpatterns = [
    path('', views.Nutrition_Home, name = 'Nutrition_Home'),
    path('Nutrition_create/', views.registerform, name = 'Nutrition_create'),
    path('<int:pk>/details/', views.userdetails, name='Nutrition_User_Details'),
    path('Nutrition_Display/', views.displayusers, name = 'Nutrition_display'),
]