
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='eb_home'),
   #path('cancel/<int:pk>', views.cancel, name='eb_cancel'),
    path('reserve/', views.reserve, name='eb_reservation'),

]