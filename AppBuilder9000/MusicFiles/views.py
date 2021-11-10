from django.shortcuts import render


# Create your views here.


def musicfiles_home(request):
    #This render function will take the request argument, and return the html document as a response

    return render(request, "musicfiles_home.html")
