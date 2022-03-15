from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ChefKnives_Home"),
]
