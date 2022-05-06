from django.urls import path
from . import views

urlpatterns = [
    path('', views.oregon_home, name='oregon_home'),
    path('Oregon_create/', views.oregon_create, name='oregon_create'),
    path('View Activities/', views.oregon_display, name='oregon_display'),
    path('Oregon_details/', views.oregon_details, name='oregon_details'),
    path('Oregon_view/', views.oregon_view, name='oregon_view'),
]
