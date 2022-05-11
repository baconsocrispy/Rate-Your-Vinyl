from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.texmex_home, name='texmex_home'),
    path('edit_recipe', views.edit_recipe, name="edit_recipe"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete', views.confirmed, name="confirmed"),
    path('createRecord', views.createRecord, name="createRecord"),
]