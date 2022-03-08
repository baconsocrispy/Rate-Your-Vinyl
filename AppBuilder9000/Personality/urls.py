from django.urls import path

from . import views

urlpatterns = [
    path('', views.personality_home, name='personality_home'),
    path('create/', views.personality_create, name='personality_create'),
    path('compare/', views.personality_compare, name='personality_compare'),
]