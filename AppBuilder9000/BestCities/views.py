from django.shortcuts import render

def Best_Cities_home(request):
    return render(request, 'BestCities/Best_Cities_home.html')
