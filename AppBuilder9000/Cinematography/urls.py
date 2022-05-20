from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.camIndex, name="Camera_home"),
    path('', views.camList, name="Camera_database"),
    path('', views.navbar, name="navbar"),
    path('content/colors', views.colors, name="colors"),
    path('content/comp', views.comp, name="comp"),
]