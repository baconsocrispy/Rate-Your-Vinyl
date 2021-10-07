from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

# the name parameter calls the linked function, while the view method displays
# given url

urlpatterns = [
    path('', views.mcharts_base, name="mcharts_base"),


]