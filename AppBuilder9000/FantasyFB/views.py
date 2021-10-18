from django.shortcuts import render

# Create your views here.

def fantasyFB_home(request):
    return render(request, 'fantasyFB_home.html')
