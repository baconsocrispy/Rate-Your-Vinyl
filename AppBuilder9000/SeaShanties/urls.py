from django.urls import path
from .import views


urlpatterns = [
    path('', views.shantieshome, name='shanties_home'),
    path('shanties_add/', views.shantiesadd, name='shanties_add'),
    path('shanties_home/', views.shantieshome, name='shanties_home'),
]
