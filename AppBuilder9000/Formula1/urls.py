from django.urls import path
from . import views

urlpatterns = [
    path('', views.f1_home, name="f1_home")
]