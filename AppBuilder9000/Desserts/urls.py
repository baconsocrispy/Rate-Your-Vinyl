from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='desserts_home'),
    path('desserts_add/', views.add_recipe, name='desserts_add'),
    path('desserts_displayDB/', views.display_recipe_items, name='desserts_displayDb'),
    path('<int:pk>/desserts_details/', views.recipe_details, name='desserts_details'),
    path('<int:pk>/desserts_edit/', views.edit_recipe, name='desserts_edit'),

]