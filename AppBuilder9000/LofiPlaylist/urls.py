from django.urls import path
from .import views

urlpatterns = [
    path('', views.lofi_home, name="lofi_home"),
    path('lofi_add/', views.lofi_add, name="lofi_add"),
    path('lofi_display/', views.lofi_display, name="lofi_display"),
    path('lofi_details/<int:pk>/', views.lofi_details, name="lofi_details"),
    path('lofi_edit/<int:pk>/', views.lofi_edit, name="lofi_edit"),
    path('confirm_delete/<int:pk>/', views.confirm_delete, name="confirm_delete"),

]

