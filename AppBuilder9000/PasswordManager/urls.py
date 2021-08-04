# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import include
# from django.contrib import admin
# Comment-in above lines as-needed
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PM_home, name='PM_home.html')
]