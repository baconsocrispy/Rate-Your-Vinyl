
from django.urls import include
from django.urls import path
from .import views

urlpatterns = [
    path('', views.KeyMaster_home, name="KeyMaster_home"),
    path('addgame/', views.KeyMasterAddGame, name='addgame'),
    path('adddlc/', views.KeyMasterAddDLC, name='adddlc'),
    path('addwish/', views.KeyMasterAddWishlist, name='addwish'),
    path('gamelist/', views.KeyMaster_Gamelist, name="gamelist"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/wish_details/', views.wish_details, name="wish_details"),

]