from django.urls import path
from . import views

urlpatterns = [
    path('', views.Character_home, name="Character_home"),
]