from django.shortcuts import render

# Create your views here.
def Recipes_Home(request):
    return render(request, 'Recipes_Home.html')