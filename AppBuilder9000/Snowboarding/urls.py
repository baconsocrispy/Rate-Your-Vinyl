from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='Snowboarding_Home'),
    path('New_Ryder/', views.AddNewRyder, name='AddNewRyder'),
    path('Ryders/', views.GetAllRyders, name='Ryders'),

]