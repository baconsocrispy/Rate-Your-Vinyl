from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BestGamesEver_Home, name='BestGamesEver_Home'),
    path('GameCreate/', views.Game_Create, name='Game_Create'),
]