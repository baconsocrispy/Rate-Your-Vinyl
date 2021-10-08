from django.urls import path
from . import views

# the name parameter calls the linked function, while the view method displays
# given url

urlpatterns = [
    path('', views.mcharts_base, name="mcharts_base"),
    path('create_chart/', views.create_chart, name="create_chart"),
    path('chart_data/', views.chart_data, name="chart_data"),
    path('<int:pk>/chart_details/', views.chart_details, name="chart_details"), # the int:pk resembles the current key for given object being viewed
                                                                                # chart_details.html

]
