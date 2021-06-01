from django.shortcuts import render


# Create your views here.
def at_home(request):
    return render(request, 'ArtistTrack_home.html')