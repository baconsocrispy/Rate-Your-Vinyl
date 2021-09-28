from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

# you invoke the name while the views.'method' page occurs on your browser
urlpatterns = [
    path('', views.eurotrip_home, name="eurotrip_home"),
   ]



