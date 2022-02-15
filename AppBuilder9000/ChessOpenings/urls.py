from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='chess_home'),

    path('add_game/', views.add_game, name="add_game"),
]
urlpatterns += staticfiles_urlpatterns()
