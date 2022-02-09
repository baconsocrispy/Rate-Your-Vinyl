from django.shortcuts import render

def MMAHome(request):
    return render(request, 'MMA_home.html')
