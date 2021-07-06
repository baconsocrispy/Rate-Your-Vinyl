from django.urls import path
from . import views

urlpatterns = [
    # imported recipe_home function from views
    path('', views.recipe_home, name='recipe_home'),
]