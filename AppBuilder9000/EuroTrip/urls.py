from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

# you invoke the name while the views.'method' page occurs on your browser
urlpatterns = [
    path('', views.eurotriphome, name="eurotriphome"),
    path('eurotrip_accomcreate/', views.eurotrip_accomcreate, name="eurotrip_accomcreate"),
    path('eurotrip_accomodations/', views.eurotrip_accomcreate, name="eurotrip_accomodations"),
    path('eurotrip_locations/', views.eurotrip_locations, name="eurotrip_locations"),
    path('eurotrip_loccreatecreate/', views.eurotrip_loccreate, name="eurotrip_loccreate"),
    path('eurotrip_pricecreate/', views.eurotrip_pricecreate, name="eurotrip_pricecreate"),
    path('eurotrip_prices/', views.eurotrip_accomcreate, name="eurotrip_prices"),
    path('eurotrip_thingtodo/', views.eurotrip_accomcreate, name="eurotrip_thingtodo"),
    path('eurotrip_ttdcreate/', views.eurotrip_accomcreate, name="eurotrip_ttdcreate")
   ]



