from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_home, name='journal_home'),
    path('create/', views.journal_create, name='journal_create'),
    path('read/', views.journal_read, name='journal_read'),
    path('<int:pk>/update/', views.journal_update, name='journal_update'),
    path('<int:pk>/delete/', views.journal_delete, name='journal_delete'),
]
