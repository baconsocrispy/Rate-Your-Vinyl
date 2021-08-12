from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardGames_home, name='BoardGames_home'),
    path('create/', views.BoardGames_create, name='BoardGames_create'),
    path('<int:pk>/details/', views.BoardGames_get, name='BoardGames_get'),
]
