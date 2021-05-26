from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.stories, name='stories'),
    path('about/', views.about, name='about'),
    path('addStory/', views.formStory, name='formStory'),
    path('addResource/', views.formResource, name='formResource'),
]

