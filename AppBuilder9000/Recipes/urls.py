from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home')
]
