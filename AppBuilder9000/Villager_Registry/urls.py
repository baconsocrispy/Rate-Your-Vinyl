from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.VillagerRegistry_Index, name="villager_home"),
    path('list_of_villagers/', views.VillagerList, name="villager_list"),
    path('island_events/', views.VillagerEvents, name="villager_events"),
    path('account/', views.VillagerAccount, name="villager_account"),
    path('create/', views.create_account, name='villager_create'),
]
