from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="RecCon_home"),
    path("Convert/", views.convert, name="RecCon_convert"),
    path("data/", views.myrecipesList, name="RecCon_myrecipes"),
]

# views.myrecipesList, name='RecCon_myrecipes'