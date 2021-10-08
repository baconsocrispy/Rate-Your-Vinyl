from django.urls import path
from . import views

# the name parameter calls the linked function, while the view method displays
# given url

urlpatterns = [
    path('', views.mcharts_base, name="mcharts_base"),
    path('create_chart/', views.create_chart, name="create_chart"),
    path('chart_data/', views.chart_data, name="chart_data"),
]
