from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users


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
        'form': form,
    }
    return render(request, 'WeatherBall/weathercreate.html', context)