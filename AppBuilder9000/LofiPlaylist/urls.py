from django.urls import path
from .import views

urlpatterns = [
    path('', views.Lofi_home, name="Lofi_home"),
]

