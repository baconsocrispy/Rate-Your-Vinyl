from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Masonry_home(request):
    # This render function will take the request argument, and return the html document as a response

    return render(request, 'Masonry_home.html')