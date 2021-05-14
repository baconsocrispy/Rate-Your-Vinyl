from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm
from .models import Song



def lofi_home(request):
    return render(request, 'lofi_home.html',)


def lofi_add(request):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lofi_display')
    return render(request, 'lofi_add.html', {'form': form})


def lofi_display(request):
    LofiPlaylist = Song.objects.all()
    return render(request, 'lofi_display.html', {'LofiPlaylist': LofiPlaylist})


def lofi_details(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'lofi_details.html', {'song': song})


def lofi_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    form = SongForm(request.POST or None, instance=song)
    if form.is_valid():
        form.save()
        return redirect('lofi_display')
    return render(request, 'lofi_edit.html', {'form': form})


def confirm_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('lofi_display')
    return render(request, 'confirm_delete.html', {'song': song})






