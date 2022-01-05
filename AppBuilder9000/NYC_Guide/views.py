from django.shortcuts import render

def home(request):
    return render(request, 'NYC_Guide/nyc_home.html')
