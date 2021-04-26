from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.new_Theater, name="new_Theater"),
    path('home/', views.Theater_home, name="Theater_home"),
    path('find/', views.find_Theater, name="find_Theater"),
]

