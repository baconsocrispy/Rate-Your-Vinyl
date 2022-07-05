from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sneakers_home, name="Sneakers_home"),
    path('create/', views.create_sneaker, name='create')
]