from django.shortcuts import render

def kettleBells(request):
    return render(request, 'kettleBells_home.html')