from django.urls import path

from . import views

# the variable showing the path to the the views function.
urlpatterns = [
    path('', views.funkocollectorhome, name='funkocollectorhome'),
    path('addcollection', views.addcollection, name='addcollection'),
    path('collection', views.collection, name='collection'),
    path('searchcollection', views.searchcollection, name='searchcollection'),

]