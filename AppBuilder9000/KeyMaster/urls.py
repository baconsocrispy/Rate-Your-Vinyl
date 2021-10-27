from django.urls import path
from .import views

urlpatterns = [
    path('', views.KeyMaster_home, name="KeyMaster_home"),
]