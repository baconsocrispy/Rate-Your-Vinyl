from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .models import Location

urlpatterns = [
    path('', views.TrackApp_home, name='TrackApp_home'),
    path('TrackApp_Add',views.TrackApp_Add, name='TrackApp_Add')

]