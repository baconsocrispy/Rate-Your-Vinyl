from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.camIndex, name="Camera_home"),
    path('Camera_database.html', views.camList, name="Camera_database"),
    path('Cinematography/navbar', views.navbar, name="navbar"),
    path('Cinematography/colors', views.colors, name="colors"),
    path('Cinematography/comp', views.comp, name="comp"),
]