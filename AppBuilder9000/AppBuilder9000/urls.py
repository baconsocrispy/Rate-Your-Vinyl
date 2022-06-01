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
    path('Books/', include('Books.urls')),
    path('MuayThai/', include('MuayThai.urls')),
    path('StockMarket/', include('StockMarket.urls')),
    path('Journal/', include('Journal.urls')),
    path('vintage_cars/', include('vintage_cars.urls')),
    path('Basketball/', include('Basketball.urls')),
    path('Seattle/', include('Seattle.urls')),
    path('Basketball/', include('Basketball.urls')),
    path('Dallas/', include('Dallas.urls')),
    path('Dogs/', include('Dogs.urls')),
    path('Oregon_City/', include('Oregon_City.urls')),
    path('EmpireBuilder/', include('EmpireBuilder.urls')),
    path('StreetLeagueSkateboarding/', include('StreetLeagueSkateboarding.urls')),
    path('All_Inclusive_Resorts/', include ('All_Inclusive_Resorts.urls')),
    path('Coach/', include('Coach_Portal.urls')),
    path('TexMex/', include('TexMex.urls')),
    path('CustomPCs/', include('CustomPcs.urls')),
    path('Nutrition/', include('Nutrition.urls')),
    path('Cinematography/', include('Cinematography.urls')),
    path('FinancialEvaluator/', include('FinancialEvaluator.urls')),
    path('Portfolio/', include('Portfolio.urls')),
    path('FitnessLog/', include('FitnessLog.urls')),
    path('Anime/', include('Anime.urls')),
]

#urlpatterns +=staticfiles_urlpatterns()

#if settings.DEBUG:  # FOR PILLOW LIBRARY
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)