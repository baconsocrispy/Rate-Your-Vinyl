from django.shortcuts import render

# Create your views here.


def novakane_home(request):
    return render(request, 'NovakaneWeather/Novakane_home.html')


def weather(request):
    return render(request, 'NovakaneWeather/Novakane_weather.html')


def radar(request):
    return render(request, 'NovakaneWeather/Novakane_radar.html')