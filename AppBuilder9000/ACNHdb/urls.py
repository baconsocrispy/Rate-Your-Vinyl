from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acnh_home, name="acnh_home"),
    path('create/', views.acnh_create, name="acnh_create"),
    path('collection/', views.acnh_collection, name="acnh_collection")
]