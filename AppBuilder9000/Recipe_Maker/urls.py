from django.urls import path
from . import views
from .views import RecipeListView

urlpatterns = [
    # imported recipe_home function from views
    path('', views.recipe_home, name='Recipe_Maker'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipes_display/', views.RecipeListView.as_view(), name='recipes_display'),
]