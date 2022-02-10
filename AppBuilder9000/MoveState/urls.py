from django.urls import path
from . import views


urlpatterns = [
    path('', views.movestate_home, name="movestate_home"),
    path('add_state/', views.add_state, name="add_state"),
    path('list_state/', views.list_state, name="list_state"),
    # path('movestate_details/', views.movestate_details, name="movestate_details"),
    # path('admin_console/', views.admin_console, name="admin_console"),
]