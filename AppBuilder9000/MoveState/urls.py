from django.urls import path



urlpatterns = [
    path('', views.movestate_home, name="movestate_home"),
    # path('state_create/', views.state_create, name="state_create"),
    # path('list_state/', views.all_state, name="list_state"),
    # path('admin_console/', views.admin_console, name="admin_console"),
]