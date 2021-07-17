from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from NBAstats import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.nba_home, name="stats-home"),
    path('display_all/', views.display_all, name="display-all"),
    path('display_2021/', views.display_2021, name="display-2021"),
    path('display_2020/', views.display_2020, name="display-2020"),
    path('display_2019/', views.display_2019, name="display-2019"),
    path('<int:pk>/details/', views.show_details, name='details'),
    path('<int:pk>/edit/', views.edit_player, name='editPlayer'),
    path('<int:pk>/delete/', views.delete_player, name='deletePlayer'),
    path('basketball-reference', views.b_ref, name='b-ref'),
    ]
