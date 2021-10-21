from django.shortcuts import render

# Create your views here.
def The_Force_home(request):
    return render(request, 'The_Force_Home.html')
