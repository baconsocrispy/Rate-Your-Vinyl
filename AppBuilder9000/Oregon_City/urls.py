from django.urls import path
from . import views

urlpatterns = [
    path('', views.oregon_home, name='oregon_home'),
    path('Oregon_create/', views.oregon_create, name='oregon_create'),
    path('display/', views.oregon_display, name='oregon_display'),
    path('<int:pk>/details/', views.oregon_details, name='oregon_details'),
    path('Oregon_view/', views.oregon_view, name='oregon_view'),
]

