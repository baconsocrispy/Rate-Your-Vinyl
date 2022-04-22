from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_home, name='journal_home'),
    path('create/', views.journal_create, name='journal_create'),
    path('read/', views.journal_read, name='journal_read'),
    path('<int:pk>/update/', views.journal_update, name='journal_update'),
    path('<int:pk>/delete/', views.journal_delete, name='journal_delete'),
    path('api/', views.journal_api, name='journal_api'),
    path('bs/', views.journal_bs, name='journal_bs'),
]
