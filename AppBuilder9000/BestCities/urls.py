from django.urls import path
from . import views

urlpatterns = [
    path('', views.Best_Cities_home, name='Best_Cities_home'), #if there is no path in the url it send them to my site's home page
    path('create/', views.Best_Cities_create, name='Best_Cities_create'), #this calls the function to create the create page
    ]