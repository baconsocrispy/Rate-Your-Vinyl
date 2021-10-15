from django.shortcuts import render

# Create your views here.
def cim_home(request):
    return render(request, 'cim_home.html')

