from django.urls import path
from . import views

urlpatterns = [
    path('', views.cards_home, name='BaseballCards_home'),
    path('add/', views.add_card, name='BaseballCards_add'),
]
