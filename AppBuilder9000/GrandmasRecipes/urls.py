from django.urls import path
from .import views


urlpatterns = [
    path('',views.GrandmasRecipes_home, name='GrandmasRecipes_home')
]