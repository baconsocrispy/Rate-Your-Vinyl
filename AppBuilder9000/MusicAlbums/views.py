from django.shortcuts import render

# Create your views here.
def MusicAlbums_home(request):
    return render(request, "MusicAlbums/MusicAlbums_home.html")
