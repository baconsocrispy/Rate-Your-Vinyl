from django.urls import path

from . import views

urlpatterns = [
    path('', views.fantasyFB_home, name='fantasyFB_home'),

]