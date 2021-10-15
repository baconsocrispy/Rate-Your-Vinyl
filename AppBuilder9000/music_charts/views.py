from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Charts
from .forms import ChartsForm
import requests
import urllib.request
from bs4 import BeautifulSoup as bs



# pulls in the data from our class Charts

# Create your views here.
# on click renders the index.html or initial page for given app.
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


def delete_event(request, event_id):  # deletes the selected row, and redirects to 'Charts'
    event = Charts.objects.get(pk=event_id)
    event.delete()
    return redirect("chart_data")


def edit_chart(request, event_id):
    changes = Charts.objects.get(pk=event_id)
    form = ChartsForm(request.POST or None, instance=changes)
    if form.is_valid():
        form.save()
        return redirect("chart_data")
    return render(request, 'music_charts/edit_chart.html', {'changes': changes, 'form': form})


def hot_one_hundred(request):
    URL = 'https://www.billboard.com/charts/hot-100'
    response = requests.get(URL)
    soup = bs(response.content, 'html.parser')
    song_data = soup.findAll('li', attrs={"class": 'chart-list__element display--flex'})

    for store in song_data:
        number = store.button.span.span.text
        titles = store.button.find('span', class_='chart-element__information')
        title2 = titles.find('span', class_='chart-element__information__song text--truncate color--primary').text
        artist = titles.find('span', class_='chart-element__information__artist text--truncate color--secondary').text
        context = {'song_data': song_data, 'titles': titles, 'rank': number, 'song': title2, 'artist': artist}

        return render(request, 'music_charts/hot_100.html', context)


