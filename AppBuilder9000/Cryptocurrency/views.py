from django.shortcuts import render

# Create your views here.

#Story #1
def Cryptocurrency_home(request):
    return render(request, "Cryptocurrency/Cryptocurrency_home.html")
