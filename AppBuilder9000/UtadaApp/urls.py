from django.urls import path
from . import views

#urls for the website
urlpatterns = [
    path('',views.home,name='hiki_home'),
    path('music',views.music,name ='hiki_music')
]