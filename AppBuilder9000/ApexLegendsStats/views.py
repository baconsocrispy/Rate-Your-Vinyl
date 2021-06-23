from django.shortcuts import render

def ApexHome(request):#my function that gives the correct html page to load when requested
    return render(request, 'ApexLegendsStats/ApexLegendsStats_home.html')