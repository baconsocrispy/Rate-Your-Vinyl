from django.urls import path
from .import views

urlpatterns = [
   path('', views.The_Force_home, name="_Home"),
   ## path('The_Force_Create/', views., name="Sushi_RecipesThe_Force_View"),
   ## path('<int:pk>/The_Force_Details/', views., name="The_Force_Details"),
   ## path('<int:pk>/The_Force_Edit/', views., name="The_Force_Edit"),
   ## path('<int:pk>/The_Force_Delete/', views., name="The_Force_Delete"),
]