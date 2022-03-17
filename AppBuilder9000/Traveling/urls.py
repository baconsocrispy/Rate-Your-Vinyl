from django.urls import path
from . import views


urlpatterns = [
    path('', views.Traveling_home,name='Traveling_home'),
]