from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name='Quotes_home'),
    path('Quotes_add/', views.Quotes_add, name="Quotes_add"),

]