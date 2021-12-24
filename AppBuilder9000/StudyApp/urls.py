from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.study_home, name='study_home'),
    path('register/', views.sign_up, name='sign_up'),
]