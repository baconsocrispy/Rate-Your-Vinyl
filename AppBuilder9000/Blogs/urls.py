# from django.urls import path, include
# from Blogs import views
#
# urlpatterns = [
#     path('', views.blogs_home, name='blogs_home'),
# ]
#

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blogs_home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]