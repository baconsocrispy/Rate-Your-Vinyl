from django.urls import path
from . import views

urlpatterns = [
    path('', views.Atv_home, name='Atv_home'),
    path('AtvTrails_create/', views.add_trail, name='add_trail'),
]
