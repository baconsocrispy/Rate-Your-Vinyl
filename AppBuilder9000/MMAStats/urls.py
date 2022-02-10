from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MMAHome, name='MMA_Home'),
    path('create/', views.MMACreate, name='MMA_Create'),
    path('stats/', views.DisplayStats, name='MMA_Stats'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)