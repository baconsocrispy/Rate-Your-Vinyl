from django.shortcuts import render

# Create your views here.

def florida_birds_home(request):
    return render(request, 'FloridaBirds/FloridaBirds_home.html')
