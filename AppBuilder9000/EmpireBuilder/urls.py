
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('', views.eb_home, name='eb_home'),
   #path('cancel/<int:pk>', views.cancel, name='eb_cancel'),
    path('reserve/', views.eb_reserve, name='eb_reservation'),

]