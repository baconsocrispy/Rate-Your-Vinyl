from django.urls import path

from . import views

# the variable showing the path to the the views function and the html page each function is for.
urlpatterns = [
    path('', views.funkocollectorhome, name='funkocollectorhome'),
    path('addcollection', views.addcollection, name='addcollection'),
    path('collection', views.collection, name='collection'),
    path('searchcollection', views.searchcollection, name='searchcollection'),
    # shows the html and the id path of the object being displayed in the url
    path('detailscollection/<funkopopname_id>', views.detailscollection, name='detailscollection'),

]