from django.shortcuts import render

# Creating views
def cultclassicsHome(request):
    return render(request, 'CultClassicsHome.html')
