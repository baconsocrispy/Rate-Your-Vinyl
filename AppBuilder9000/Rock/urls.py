from django.urls import path
from . import views

urlpatterns = [
    path('', views.RocksHome, name='RocksHome'),
    path('admin/', admin.site.urls),

]