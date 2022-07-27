from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='VinylCollection_home'),
    path('createRelease', views.create_release, name='createRelease'),
    path('collection/', views.collection, name='collection'),
    path('<int:pk>/details/', views.details, name='details'),
]
