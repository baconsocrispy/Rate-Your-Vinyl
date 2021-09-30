from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

# you invoke the name while the views.'method' page occurs on your browser
urlpatterns = [
    path('', views.eurotriphome, name="eurotriphome"),
    path('eurotrip_loccreate/', views.eurotrip_loccreate, name="eurotrip_loccreate"),
   ]



