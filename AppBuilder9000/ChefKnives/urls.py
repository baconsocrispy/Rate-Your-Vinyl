from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ChefKnives_Home"),
    path('ChefKnives_Create/', views.chefknives_create, name="ChefKnives_Create"),
    path('ChefKnives_View/', views.chefknives_view, name="ChefKnives_View"),


]
