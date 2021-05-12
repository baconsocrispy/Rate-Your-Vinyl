from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song


def lofi_home(request):
    return render(request, 'lofi_home.html',)


def lofi_add(request):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lofi_home')
    else:
        print(form.errors)
        form = SongForm()
    context = {
        'form': form,
    }
    return render(request, 'lofi_add.html', context)








