from django.urls import path
from . import views


urlpatterns = [
    # imported recipe_home function from views
    path('', views.recipe_home, name='Recipe_Maker'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('list_recipes/', views.list_recipes, name='list_recipes'),
    path('details/', views.details, name='details'),
]