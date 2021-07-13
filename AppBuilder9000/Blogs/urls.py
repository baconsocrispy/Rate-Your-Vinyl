from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('entry/', views.new_entry, name='entry'),
]
