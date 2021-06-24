from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name='Quotes_home'),
    path('Quotes_add/', views.Quotes_add, name="Quotes_add"),
    path('Quotes_display/', views.Quotes_display, name="Quotes_display"),
    path('Quotes_details/<int:pk>/', views.Quotes_details, name="Quotes_details"),
]