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
    path('', views.home, name='home'),
    path('HotSprings/', include('HotSprings.urls')),
    path('Rock/', include('Rock.urls')),
    path('Masonry/', include('Masonry.urls')),
    path('Campsites/', include('Campsites.urls')),
    path('CampingSupplies/', include('CampingSupplies.urls')),
    path('Gardening/', include('Gardening.urls')),
    path('BitcoinAnalytics', include('BitcoinAnalytics.urls')),
    path('BasketballStats', include('BasketballStats.urls')),
    path('Stocks/', include('Stocks.urls')),
    path('DNDCharacters', include('DNDCharacters.urls')),
    path('Practicing_Yoga/', include('Practicing_Yoga.urls')),
    path('StudyApp/', include('StudyApp.urls')),
    path('CryptoAnalytics/', include('CryptoAnalytics.urls')),
    path('PetAdoption', include('PetAdoption.urls')),
    path('MusicReviews/', include('MusicReviews.urls')),
    path('NYC_Guide/', include('NYC_Guide.urls')),
    path('Hiphop/', include('Hiphop.urls')),
    path('PokeDex/', include('PokeDex.urls')),
    path('BestCities/', include('BestCities.urls')),
    path('WeatherBall/', include('WeatherBall.urls')),
]

#urlpatterns +=staticfiles_urlpatterns()

#if settings.DEBUG:  # FOR PILLOW LIBRARY
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)