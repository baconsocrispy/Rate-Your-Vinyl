from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'MovieReviews/moviereviews_home.html')
