from django.urls import path
from . import views

urlpatterns = [
    path('', views.MagicTheGathering_home, name='MagicTheGathering_home')
    ]