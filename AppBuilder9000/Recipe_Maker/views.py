from django.shortcuts import render


# first instruction on what to do if "home" get invoked
def home(request):
    # renders in the browser
    return render(request, 'Recipe_Maker/Recipe_Maker_home.html')