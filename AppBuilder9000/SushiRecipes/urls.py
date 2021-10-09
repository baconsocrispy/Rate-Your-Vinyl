from django.urls import path
from .import views

urlpatterns = [
    path('', views.sushi_recipes_home, name="Sushi_Recipes_Home"),
    path('Sushi_Recipes_Create/', views.sushi_recipes_create, name="Sushi_Recipes_Create"),
    path('Sushi_Recipes_View/', views.sushi_recipes_view, name="Sushi_Recipes_View"),
]
