from django.shortcuts import render, redirect
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist

def home(request):
    return render(request, 'VinylCollection/home.html')

def create_release(request):
    form = ReleaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('VinylCollection_home')
    else:
        print(form.errors)
        form = ReleaseForm()
    context = {
        'form': form,
    }
    return render(request, 'VinylCollection/createRelease.html', context)

def collection(request):
    releases = Release.objects.all()
    context = {
        'releases': releases,
    }
    return render(request, 'VinylCollection/collection.html', context)
