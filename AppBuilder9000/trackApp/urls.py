from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .models import TrackApp
from .forms import TrackAppForm

urlpatterns = [
    path('', views.TrackApp_home, name='TrackApp_home'),
    path('', Retrieve_TrackApp_detail, name='TrackApp_detail.html'),
    path('', Retrieve_TrackApp_create, name='TrackApp_create.html'),
]