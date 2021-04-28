from django.shortcuts import render

# Create your views here.
def Character_home(request):
    return render(request, "Character_home.html")