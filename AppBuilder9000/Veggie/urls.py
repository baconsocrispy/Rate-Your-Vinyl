from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.veggie_home, name="Veggie_home"),                                     # home page
    path('veggie_form/', views.create_recipe, name="veggie_form"),                       # adding new recipe page
    path('veggie_recipe/', views.display_veggie, name="veggie_recipe"),                  # displays all recipes page
    path('<int:pk>/veggie_details/', views.single_recipe, name="veggie_details"),        # display one recipe
]
