from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="gamereviews_home"),
    path('gamereviews_addreview/', views.add_review, name="gamereviews_addreview"),
]
