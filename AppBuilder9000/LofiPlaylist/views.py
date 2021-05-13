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
    context = {
        'form': form,
    }
    return render(request, 'lofi_add.html', context)


def lofi_display(request):
    LofiPlaylist = Song.objects.all()
    return render(request, 'lofi_display.html', {'LofiPlaylist': LofiPlaylist})


def lofi_details(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'lofi_details.html', {'song': song})




