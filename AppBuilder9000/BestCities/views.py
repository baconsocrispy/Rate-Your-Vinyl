from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlacesForm
from .models import Places
from django.http import JsonResponse
import requests
import json


def Best_Cities_home(request): #function to render the home page
    return render(request, 'BestCities/Best_Cities_home.html')

def Best_Cities_create(request): #function to add a city to the database
    form = PlacesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Best_Cities_home')
    else:
        print(form.errors)
        form = PlacesForm()
    context = {
        'form': form
    }
    return render(request, 'BestCities/Best_Cities_create.html', context)

def Best_Cities_topcities(request):
    topC = Places.objects.all()
    return render(request, 'BestCities/Best_Cities_topcities.html', {'topC': topC})

def Best_Cities_details(request, pk):
    item = get_object_or_404(Places, pk=pk)
    return render(request, 'BestCities/Best_Cities_details.html', {'item': item})

def Best_Cities_edit(request, pk):
    item = get_object_or_404(Places, pk=pk)
    form = PlacesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Best_Cities_topcities')
        else:
            print(form.errors)
    else:
        return render(request, 'BestCities/Best_Cities_edit.html', {'form': form, 'item': item})

def Best_Cities_delete(request, pk):
    change = get_object_or_404(Places, pk=pk)
    if request.method == 'POST':
        change.delete()
        return redirect('Best_Cities_topcities')
    context = {"change": change}
    return render(request, 'BestCities/Best_Cities_delete.html', context)

def Best_Cities_confirmed(request):
    if request.method == 'POST':
        form = PlacesForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Best_Cities_topcities')
    else:
        return redirect('Best_Cities_home')

def Best_Cities_weather(request):
    info = []

    if request.method == 'POST':
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q": request.POST['searchTerm'], "units": "imperial", "mode": "JSON"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "be30be0618mshf5d1c84d0650830p17fd71jsn7b66e52ac477"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        weather = json.loads(response.text)

        name = weather['name']
        info.append(name)
        main_info = weather['main']
        temperature = main_info['temp']
        info.append(temperature)
        feelsT = main_info['feels_like']
        info.append(feelsT)
        TH = main_info['temp_max']
        info.append(TH)
        TL = main_info['temp_min']
        info.append(TL)
        Wind = weather['wind']['speed']
        info.append(Wind)
        THumid = main_info['humidity']
        info.append(THumid)

    CTemp = request.POST.get('CurrentTemp', '') == 'on'
    print(CTemp)
    FT = request.POST.get('feelsTemp', '') == 'on'
    print(FT)
    TH = request.POST.get('THigh', '') == 'on'
    print(TH)
    TL = request.POST.get('TLow', '') == 'on'
    print(TL)
    WindSpeed = request.POST.get('Wind', '') == 'on'
    print(WindSpeed)
    THumid = request.POST.get('Hum', '') == 'on'
    print(THumid)

    context = {
        'info': info, 'CTemp': CTemp, 'FT': FT, 'TH': TH, 'TL': TL,
        'WindSpeed': WindSpeed, 'THumid': THumid
    }


    return render(request, 'BestCities/Best_Cities_weather.html', context)

