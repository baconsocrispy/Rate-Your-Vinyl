# from django.urls import path, include
# from Blogs import views
#
# urlpatterns = [
#     path('', views.blogs_home, name='blogs_home'),
# ]
#
from requests import request

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blogs_home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # i dont know why this doesnt need a path. maybe it does?
    # all i know is as_view is a view as a class but i dont know what that means
    path('', views.new_post(request), name='blogs_new'),
]