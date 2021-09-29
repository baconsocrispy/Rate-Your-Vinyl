from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from .import views
# invoking the name while views.'method' page occurs on browser
urlpatterns = [
    path('', views.cultclassicsHome, name="cultclassicsHome"),
]