from django.urls import path
from . import views
from .views import ReleaseUpdateView, ReleaseDeleteView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='VinylCollection_home'),
    path('createRelease', views.create_release, name='createRelease'),
    path('collection/', views.collection, name='collection'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/edit/', ReleaseUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ReleaseDeleteView.as_view(), name='delete'),
    path('add_album/', views.add_album, name='add_album'),
    path('confirm_add', views.confirm_add, name='confirm_add'),
    path('scores/', views.display_scores, name='scores'),
]
