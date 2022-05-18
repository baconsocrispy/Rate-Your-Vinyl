from django.shortcuts import render

def Nutrition_Home(request):
    return render(request, "Nutrition/Nutrition_Home.html")
