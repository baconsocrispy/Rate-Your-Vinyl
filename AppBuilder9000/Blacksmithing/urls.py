from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blacksmithing_Home, name='Blacksmithing_Home'),
    path('ToolCreate/', views.Tool_Create, name='Tool_Create'),
    path('ViewTools/', views.View_Tools, name='Tool_View'),
    path('<tool_id>/details/', views.Tool_Details, name='Tool_Details'),
    path('<tool_id>/edit/', views.Edit_Tools, name='Edit_Tools'),
    path('<tool_id>/delete/', views.Delete_Tools, name='Delete_Tools'),
]
