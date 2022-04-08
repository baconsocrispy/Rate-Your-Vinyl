from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.f1_home, name="f1_home"),
    path('add_result/', views.add_result, name="add_result"),
    path('result_submit/', views.result_submit, name="result_submit"),
    path('admin/', admin.site.urls),
]