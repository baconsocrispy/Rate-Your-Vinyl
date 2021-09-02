from django.urls import path
from . import views

urlpatterns = [
    path('', views.blazerstats_home, name='blazerstats_home'),
    path('Blazercreate/', views.blazerstats_create, name='blazerstats_create'),
    path('Players/', views.blazerstats_players, name='blazerstats_players'),
    path('<int:pk>/details/',views.blazerstats_details, name='blazerstats_details'),
]