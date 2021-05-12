from django.urls import path
from .import views

urlpatterns = [
    path('', views.lofi_home, name="lofi_home"),
    path('lofi_add/', views.lofi_add, name="lofi_add"),
    path('lofi_display/', views.lofi_display, name="lofi_display")
]

