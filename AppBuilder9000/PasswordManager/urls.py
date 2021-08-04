# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import include
# from django.contrib import admin
# Comment-in above lines as-needed
from django.urls import path
from . import views


urlpatterns = [ # stores the routes/paths within the project; the'WHEN' what's in'PasswordManager/templates/views.py' gets displayed
    path('', views.PM_home, name='PasswordManager_home'),
]