from django.urls import path
from . import views


urlpatterns = [
    path('', views.grandmas_recipes_home, name='GrandmasRecipes_home'),
    path('/library', views.grandmas_recipes_library, name='GrandmasRecipes_library'),
    path('/AddNew', views.grandmas_recipes_addNew, name='GrandmasRecipes_addnew'),
]
