from django.urls import path
from . import views

# the directory of . is our current directory
# so the above says import views.py from the current directory

urlpatterns = [
    path('', views.Dogs_home, name='Dogs_home'),
    path('create/', views.Dogs_create, name='create'),
]