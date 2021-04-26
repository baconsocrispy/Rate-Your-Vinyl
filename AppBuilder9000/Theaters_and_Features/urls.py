from django.urls import path
from . import views

urlpatterns = [
    path('', views.Theater_home, name='Theater_home'),
    path('add/', views.new_Theater, name="new_Theater"),
    path('home/', views.Theater_home, name="Theater_home"),
]

