from django.urls import path

from . import views

# the variable showing the path to the the views function.
urlpatterns = [
    path('', views.funkocollectorhome, name='funkocollectorhome'),
]