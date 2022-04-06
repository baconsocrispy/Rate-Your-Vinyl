from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1_home(request):
    return render(request, "Formula1/Formula1_home.html")


