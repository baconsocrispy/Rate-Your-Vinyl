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
    path('BasketballStats/', include('BasketballStats.urls')),
    path('IceHockey/', include('IceHockey.urls')),
    path('Composers/', include('Composers.urls')),
    path('ATVTrails/', include('ATVTrails.urls')),
    path('Motorcycling/', include('Motorcycling.urls')),
    path('FootballStats/', include('FootballStats.urls')),
    path('GameReviews/', include('GameStats.urls')),
    path('MoveState/', include('MoveState.urls')),
    path('MMAStats/', include('MMAStats.urls')),
    path('EFT_Items/', include('EFT_Items.urls')),
    path('Vehicles/', include('Vehicles.urls')),
    path('Desserts/', include('Desserts.urls')),
    path('StockTracker/', include('StockTracker.urls')),
    path('WorkoutEquipment/', include('WorkoutEquipment.urls')),
    path('StarWatch/', include('StarWatch.urls')),
    path('Drones/', include('Drones.urls')),
    path('Personality/', include('Personality.urls')),
    path('GrandmasRecipes/', include('GrandmasRecipes.urls')),
    path('SuperCars/', include('SuperCars.urls')),
    path('ChefKnives/', include('ChefKnives.urls')),
    path('Traveling/', include('Traveling.urls')),
    path('HousingCosts/', include('HousingCosts.urls')),
    path('HikingTrails/', include('HikingTrails.urls')),
    path('RecordCollection/', include('RecordCollection.urls')),
    path('Prowrestlers/', include('Prowrestlers.urls')),
    path('Cartoons/', include('Cartoons.urls')),
]

#urlpatterns +=staticfiles_urlpatterns()

#if settings.DEBUG:  # FOR PILLOW LIBRARY
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)