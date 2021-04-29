from django.urls import path
from . import views

urlpatterns = [
    path('', views.Character_home, name="Character_home"),
    path('add', views.Character_add, name="Character_add"),
    path('success', views.Character_success, name="Character_success"),
]