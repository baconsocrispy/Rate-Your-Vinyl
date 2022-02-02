from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.composers, name='composers_home'),
    path('composers_create', views.create_composer, name='composers_create'),
    path('<int:pk>/composers_details', views.composers_details, name='composer_details'),
]