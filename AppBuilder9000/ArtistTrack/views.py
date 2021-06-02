from django.shortcuts import render, redirect
from . forms import SongForm, PlaylistForm



# Create your views here.
def at_home(request):
    return render(request, 'ArtistTrack_home.html')


def add_song(request):
    form = SongForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add_song')
    content = {'form': form}
    return render(request, 'ArtistTrack_addSong.html', content)


def add_playlist(request):
    form = PlaylistForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add_playlist')
    content = {'form': form}
    return render(request, 'ArtistTrack_addPlaylist.html', content)