from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BestGamesEver_Home, name='BestGamesEver_Home'),
    path('GameCreate/', views.Game_Create, name='Game_Create'),
    path('ViewGames/', views.Game_View, name='Game_View'),
    path('<game_id>/details/', views.Game_Details, name='Game_Details'),
]