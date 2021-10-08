from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Charts
from .forms import ChartsForm
import requests
# pulls in the data from our class Charts

# Create your views here.
def mcharts_base(request):
    return render(request, 'music_charts/mcharts_base.html')

def create_chart(request):
    form = ChartsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create_chart')
    else:
        return render(request, 'music_charts/create_chart.html', {'form': form})

def chart_data(request):
    data = Charts.objects.all()

    return render(request, 'music_charts/chart_data.html', {'data': data})
