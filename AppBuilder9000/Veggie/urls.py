from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.veggie_home, name="Veggie_home"),
    path('recipe_form/', views.create_recipe, name="recipe_form"),
    path('veggie_recipe/', views.display_veggie, name="veggie_recipe"),
]
