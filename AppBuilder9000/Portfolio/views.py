from django.shortcuts import render

def PortfolioIndex(request):
    return render(request, "Portfolio_home.html")

def navbar(request):
    return render(request, "Portfolio/navbar.html")