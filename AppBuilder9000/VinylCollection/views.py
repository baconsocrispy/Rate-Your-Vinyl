from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist

class ReleaseUpdateView(UpdateView):
    model = Release
    fields = '__all__'
    success_url = reverse_lazy('collection')

class ReleaseDeleteView(DeleteView):
    model = Release
    success_url = reverse_lazy('collection')

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

def details(request, pk):
    pk = int(pk)
    release = get_object_or_404(Release, pk=pk)
    context = {
        'release': release
    }
    return render(request, 'VinylCollection/details.html', context)


