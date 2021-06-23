from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='swu_home'),
    path('sources', views.sources, name='swu_sources'),
    path('characters', views.characters, name='swu_characters'),
]
