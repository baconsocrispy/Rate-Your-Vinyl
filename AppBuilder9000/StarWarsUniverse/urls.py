from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='swu_home'),
    path('sources', views.sources, name='swu_sources'),
    path('characters', views.characters, name='swu_characters'),
    path('characters_list', views.characters_list, name='characters_list'),
    path('<id>', views.character_details, name='character_details'),
]
