from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from .forms import UsersForm
from bs4 import BeautifulSoup
import requests

def weather_home(request):
    return render(request, 'WeatherBall/weatherhome.html')

def weather_create(request):
    form = UsersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('weather_home')
    else:
        print(form.errors)
        form = UsersForm()
    context = {
        'form': form
    }
    return render(request, 'WeatherBall/weathercreate.html', context)

def weather_db(request):
    display = Users.objects.all()
    context = {
        'display': display
    }
    return render(request, 'WeatherBall/weatherdisplaydb.html', context)

def weather_details(request, pk):
    details = get_object_or_404(Users, pk=pk)
    context = {'details': details}
    return render(request, 'WeatherBall/weatherdetails.html', context)

def weather_edit(request, pk):
    edit = get_object_or_404(Users, pk=pk)
    form = UsersForm(data=request.POST or None, instance=edit)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('weather_home')
        else:
            print(form.errors)
            form = UsersForm()
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WeatherBall/weatheredit.html', context)

def weather_delete(request, pk):
    item = get_object_or_404(Users, pk=pk)
    form = UsersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('weather_db')
    return render(request, 'WeatherBall/weatherdelete.html', {'item': item, 'form': form})

def weather_scraping(request):
    seven_day_forecast = []
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=35.3434&lon=-90.2983")
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    for i in forecast_items:
        forecast = i.find('p').get_text()
        seven_day_forecast.append(forecast)
    print(seven_day_forecast)
    return render(request, 'WeatherBall/weatherscraping.html')