
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IceHockey_home, name='IceHockey_home'),
    path('newprofile', views.IceHockey_newprofile, name='IceHockey_newprofile'),
    path('myprofile', views.IceHockey_myprofile, name='IceHockey_myprofile'),
    path('<int:pk>/details/', views.IceHockey_details, name='IceHockey_details'),
    path('<int:pk>/edit/', views.IceHockey_edit, name='IceHockey_edit'),
    path('<int:pk>/delete/', views.IceHockey_delete, name='IceHockey_delete'),
    path('<int:pk>/scrapeddata/', views.IceHockey_scrapeddata, name='IceHockey_scrapeddata'),
    path('samplescrape', views.IceHockey_samplescrape, name='IceHockey_samplescrape'),
    path('sampleapi', views.IceHockey_sampleapi, name='IceHockey_sampleapi'),
    path('<int:pk>/api_page', views.IceHockey_api_page, name='IceHockey_api_page'),
    path('<int:pk>/error', views.IceHockey_error, name='IceHockey_error'),

]