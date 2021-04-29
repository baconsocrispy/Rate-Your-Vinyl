from django.urls import path
from . import views

urlpatterns = [
    path('', views.Character_home, name="Character_home"),
    path('add', views.Character_add, name="Character_add"),
    path('viewing', views.Character_view, name="Character_view"),
    path('list_all', views.Character_list, name="Character_list"),
]