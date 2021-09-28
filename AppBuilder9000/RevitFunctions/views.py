#story1, step4: Add function to views to render the home page
# add function with name matching urls.py views.xxxx (match xxxx), url will call this function and display something on the screen.

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def RevitFunctions_home(request):
    return render(request, 'RevitFunctions/RevitFunctions_home.html')


def RevitFunctions_futureNav1(request):
    return render(request, 'RevitFunctions/RevitFunctions_futureNav1.html')

def RevitFunctions_futureNav2(request):
    return render(request, 'RevitFunctions/RevitFunctions_futureNav2.html')

def RevitFunctions_futureNav3(request):
    return render(request, 'RevitFunctions/RevitFunctions_futureNav3.html')
