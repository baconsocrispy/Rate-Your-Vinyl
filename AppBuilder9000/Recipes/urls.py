from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home'),
    path('create/', views.recipes_create, name='recipes_create'),
    path('display/', views.recipes_display, name='recipes_display')
]
