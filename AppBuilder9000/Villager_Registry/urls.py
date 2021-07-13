from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.VillagerRegistry_Index, name="villager_home"),
    path('list_of_villagers/', views.VillagerList, name="villager_list"),
    path('account/', views.VillagerAccount, name="villager_account"),
    path('create/', views.create_account, name='villager_create'),
    path('villager_playerList/', views.Retrieve_PlayerList, name="villager_playerList"),
    path('<int:pk>/villager_playerDetails/', views.Retrieve_PlayerDetails, name="villager_playerDetails"),
    path('<int:pk>/villager_delete/', views.delete, name="villager_delete"),
    path('confirmed/', views.confirmed, name="villager_confirmed"),
]
