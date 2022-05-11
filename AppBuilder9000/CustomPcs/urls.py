from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomPcs_home, name='CustomPcs_Home'),

]
