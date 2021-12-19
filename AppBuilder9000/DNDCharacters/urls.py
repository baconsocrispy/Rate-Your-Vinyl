from django.urls import path
from . import views

urlpatterns = [
    path('', views.dnd_characters_home, name='dnd_characters_home'),
    path('', views.dnd_characters_howto, name="dnd_characters_HowTo"),
    path('', views.dnd_characters_classdescript, name="dnd_characters_ClassDescript"),
    path('createCharacter', views.createCharacter, name="createCharacter"),
    path('admin_console', views.admin_console, name="admin_console"),
]