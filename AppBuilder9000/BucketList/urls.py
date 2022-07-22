from django.urls import path
from . import views

urlpatterns = [
    path('', views.BucketList_home, name='BucketList_home'),
    path('create', views.BucketList_create, name='BucketList_create'),
    path('list', views.BucketList_list, name='BucketList_list'),
]
