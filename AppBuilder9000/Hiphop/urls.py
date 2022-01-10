from django.urls import path
from . import views


urlpatterns = [
    path('', views.hiphop_home, name='hiphop_home'),
    path('hiphop_create/', views.create_choose, name='hiphopviews_view'),
]
