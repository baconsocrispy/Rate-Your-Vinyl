from django.urls import path
from . import views


urlpatterns = [
    path('', views.CFB_Home, name='CFB_Home'),
    path('CreateFan/', views.CFB_AddFan, name='CFB_Add_Fan'),
]