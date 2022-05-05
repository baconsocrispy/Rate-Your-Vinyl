from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def jobsHome(request):
    return render(request, 'Jobs/jobsHome.html')