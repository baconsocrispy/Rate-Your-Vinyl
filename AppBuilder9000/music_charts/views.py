from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Charts
from .forms import ChartsForm
import requests
# pulls in the data from our class Charts

# Create your views here.
# on click renders the index.html or initial page for given app.
def mcharts_base(request):
    return render(request, 'music_charts/mcharts_base.html')

def mcharts_home(request):
    return render(request, 'music_charts/mcharts_home.html')

# on click displays update page, when form is created AND is valid it submits and returns to update page.
def create_chart(request):
    form = ChartsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create_chart')
    else:
        return render(request, 'music_charts/create_chart.html', {'form': form})

# on click renders charts page with data created in update page if any.
def chart_data(request):
    data = Charts.objects.all()

    return render(request, 'music_charts/chart_data.html', {'data': data})

# renders a details form with corresponding integer key, per created item, as a separate html.
def chart_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Charts, pk=pk)
    form = ChartsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            confirm = form.save(commit=False)
            confirm.save()
            return redirect('chart_data')
        else:
            print(form.errors)
    else:
        return render(request, 'music_charts/chart_details.html', {'form': form})


def delete_event(request, event_id): # deletes the selected row, and redirects to 'Charts'
    event = Charts.objects.get(pk=event_id)
    event.delete()
    return redirect("chart_data")
