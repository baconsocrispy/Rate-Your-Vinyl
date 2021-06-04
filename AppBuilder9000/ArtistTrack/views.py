from django.shortcuts import render, redirect, get_object_or_404
from . forms import SongForm, PlaylistForm
from . models import Song, Playlist


def at_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Song, pk=pk)
    context = {'song': item}
    return render(request, 'ArtistTrack_details.html', context)


def at_library(request):
    songs = Song.Songs.all()
    playlists = Playlist.Playlists.all()
    content = {
        'songs': songs,
        'playlists': playlists,
    }
    return render(request, 'ArtistTrack_library.html', content)


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


