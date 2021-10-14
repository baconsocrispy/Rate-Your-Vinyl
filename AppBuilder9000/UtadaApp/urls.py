from django.urls import path
from . import views

#urls for the website
urlpatterns = [
    path('',views.home,name='hiki_home'),
]