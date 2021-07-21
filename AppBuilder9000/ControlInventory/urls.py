from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ControlInventory_home'),
    path('create/', views.createuser, name='ControlInventory_account.html'),
    path('add', views.addproduct, name='ControlInventory_addproduct.html'),
    path("info/<int:pk>/", views.productinfo, name='ControlInventory_productinfo.html'),
]