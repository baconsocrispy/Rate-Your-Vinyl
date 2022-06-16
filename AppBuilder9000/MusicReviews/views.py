from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Music Review's index.")
# Create your views here.
#
def MusicReviews_home(request):
    return render(request, 'MusicReviews/MusicReviews_home.html')

# Create your views here.
