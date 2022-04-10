from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="FictionalCharacters_Home"),
    path('FictionalCharacters_Create/', views.characters_create, name="FictionalCharacters_Create"),
    path('FictionalCharacters_CreateSeries/', views.series_create, name="FictionalCharacters_CreateSeries"),
    path('FictionalCharacters_View/', views.list_characters, name="FictionalCharacters_View"),
    path('FictionalCharacters_Search/', views.search_characters, name="FictionalCharacters_Search"),
    path('FictionalCharacters_ShowChar/<char_id>', views.show_char, name="FictionalCharacters_ShowChar"),
    path('FictionalCharacters_Edit/<char_id>', views.edit_char, name="FictionalCharacters_Edit"),
    path('FictionalCharacters_Delete/<char_id>', views.delete_char, name="FictionalCharacters_Delete"),
    path('FictionalCharacters_API', views.fc_api, name="FictionalCharacters_API"),
]
