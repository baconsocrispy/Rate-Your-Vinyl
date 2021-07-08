from django.urls import path, include
from Blogs import views

urlpatterns = [
    path('', views.blogs_home, name='blogs_home'),
]
