from django.shortcuts import render


# Create your views here.
def basketballHome(request):
    return render(request, 'Basketball/Basketball_home.html')