from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
#this addition gives access to the 'include()' function that we use below in urlpatterns
from django.contrib import admin
from django.urls import path
from . import views #the directory of . is our current directory
#so the above says import views.py from the current directory
#ANATOMY OF A URL ROUTE:
#('pattern to watch for',method to call,"shortcut name")
urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('', views.nutrition_home, name="home"),#call details() and pass in pk

    #when it sees name="createRecord" it knows to go to the views.createRecord method and
    #change the name of the URL to include createRecord