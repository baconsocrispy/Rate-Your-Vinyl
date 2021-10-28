from django.urls import path
from .import views

urlpatterns = [
    path('', views.KeyMaster_home, name="KeyMaster_home"),
    path('addgame/', views.KeyMasterAddGame, name='addgame'),
    path('adddlc/', views.KeyMasterAddDLC, name='adddlc'),
    path('addwish/', views.KeyMasterAddWishlist, name='addwish'),


]