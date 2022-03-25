from django.shortcuts import render

# Create your views here.
def wrestlers_home(request):
    return render(request, 'Prowrestlers/ProWrestling_home.html')