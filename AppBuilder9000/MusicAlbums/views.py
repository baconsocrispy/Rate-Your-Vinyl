from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# Create your views here.
def MusicAlbums_home(request):
    return render(request, "MusicAlbums/MusicAlbums_home.html")

def MusicAlbums_add(request):
    form = AlbumForm(data=request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect("MusicAlbums_add")
        content={'form': form}
        return render(request, "MusicAlbums/MusicAlbums_add.html", content)