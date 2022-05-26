from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_home, name='anime_home'),
]

urlpatterns += staticfiles_urlpatterns()
