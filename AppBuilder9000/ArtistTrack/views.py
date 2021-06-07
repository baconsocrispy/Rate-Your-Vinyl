from django.shortcuts import render, redirect, get_object_or_404
from . forms import SongForm, PlaylistForm
from . models import Song, Playlist
import requests

#
# def at_api(request):
#     response = requests.get("")
#     song_data = response.json()


def at_playlist_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('at_library')
    context = {'item': item}
    return render(request, "ArtistTrack_deletePlaylist.html", context)


def at_playlist_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Playlist, pk=pk)
    form = PlaylistForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('at_library')
        else:
            print(form.errors)
    else:
        return render(request, 'ArtistTrack_playlistDetails.html', {'form': form})


def at_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('at_library')
    context = {'item': item}
    return render(request, "ArtistTrack_deleteSong.html", context)


def at_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Song, pk=pk)
    form = SongForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('at_library')
        else:
            print(form.errors)
    else:
        return render(request, 'ArtistTrack_details.html', {'form': form})


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


