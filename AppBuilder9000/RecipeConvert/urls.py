from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="RecCon_home"),
    path("add/", views.convert, name="RecCon_convert"),
]
