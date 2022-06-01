from django.shortcuts import render
from django.http import HttpResponse


# calls the Dogs_home home page when requested
def Dogs_home(request):
    return render(request, 'Dogs/Dogs_home.html')
