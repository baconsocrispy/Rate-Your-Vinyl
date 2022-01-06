from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nyc_guide_home'),
    path('add/', views.add_rest, name='add_rest'),
]