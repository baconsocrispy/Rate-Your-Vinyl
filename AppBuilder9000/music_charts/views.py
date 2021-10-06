from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# pulls in the data from our class Charts

# Create your views here.
def mcharts_base(request):
    return render(request, 'music_charts/mcharts_base.html',)