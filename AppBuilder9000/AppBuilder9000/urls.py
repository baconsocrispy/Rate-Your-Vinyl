"""AppBuilder9000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings    #FOR PILLOW LIBRARY
#from django.conf.urls.static import static     #FOR PILLOW LIBRARY
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("OregonRocks.urls")),
    path('', views.home, name='home'),
    path('music_charts/', include('music_charts.urls')),
    path('OregonRocks/', include('OregonRocks.urls')),
    path('CoreItemManagement/', include('CoreItemManagement.urls')),
    path('ValItems/', include('ValItems.urls')),
    path('UtadaHikaru/', include('UtadaApp.urls')),
    path('FunkoCollector/', include('FunkoCollector.urls')),
    path('FantasyFB/', include('FantasyFB.urls')),
    path('SportsCars/', include('SportsCars.urls')),
    path('theforce/', include('theforce.urls')),
    path('AnimeReviews/', include('AnimeReviews.urls')),
    path('KeyMaster/', include('KeyMaster.urls')),
    path('CocktailRecipes/', include('CocktailRecipes.urls')),
    path('FloridaBirds/', include('FloridaBirds.urls')),
    path('SpeedRun/', include('SpeedRun.urls')),
    path('Snowboarding/', include('Snowboarding.urls')),
    path('HotSprings/', include('HotSprings.urls')),
    path('MusicFiles/', include('MusicFiles.urls')),
    path('Rock/', include('Rock.urls')),
    path('Todo/', include('Todo.urls')),
]

#urlpatterns +=staticfiles_urlpatterns()

#if settings.DEBUG:  # FOR PILLOW LIBRARY
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)