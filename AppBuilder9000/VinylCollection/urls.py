from django.urls import path
from . import views
from .views import ReleaseUpdateView, ReleaseDeleteView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='VinylCollection_home'),
    path('createRelease', views.create_release, name='createRelease'),
    path('collection/', views.collection, name='collection'), # refactor as indexview class
    path('<int:pk>/details/', views.details, name='details'), # refactor as detailsview class
    path('<int:pk>/update/', ReleaseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ReleaseDeleteView.as_view(), name='delete'),
    path('confirm_add', views.confirm_add, name='confirm_add'),
    path('scores/', views.scores, name='scores'),
    path('get_album/', views.get_discogs_and_pitchfork_data, name='get_album'),
]
