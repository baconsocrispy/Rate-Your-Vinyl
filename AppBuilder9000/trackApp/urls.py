from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .models import Location
from .models import create

urlpatterns = [
    path('', views.TrackApp_home, name='TrackApp_home'),
    path('',views.TrackApp_Add, name='TrackApp_Add'),
    path('',views.TrackApp_create, name='TrackApp_create'),
    path('', views.TrackApp_nav, name='TrackApp_nav')

]