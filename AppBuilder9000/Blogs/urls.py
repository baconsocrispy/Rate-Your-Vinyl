from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blog'),
    path('entry/', views.new_entry, name='entry'),
]
