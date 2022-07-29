from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist
from bs4 import BeautifulSoup
import requests
import pandas


# my user token to access discogs API
DISCOGS_TOKEN = "DBiUmQgyHHBGmXsybviPrgmVVSJmMDdhpxBAGwle"

class ReleaseUpdateView(UpdateView):
    model = Release
    fields = '__all__'
    success_url = reverse_lazy('collection')

class ReleaseDeleteView(DeleteView):
    model = Release
    success_url = reverse_lazy('collection')

def home(request):
    return render(request, 'VinylCollection/home.html')

# release catalog number entry form
def add_album(request):
    return render(request, 'VinylCollection/add_album.html')

# displays release info from discogs to ensure it's correct
def confirm_add(request):
    cat_number = request.POST['cat_number']
    release = get_release(cat_number)
    blank_form = ReleaseForm()
    release_form = populate_form(release, blank_form)
    score = get_score(release)
    context = {
        'release': release,
        'form': release_form,
        'score': score,
    }
    print(release)
    return render(request, 'VinylCollection/confirm_add.html', context)

# auto-populates release form with data pulled from discogs api
def populate_form(release, blank_form):
    form = blank_form
    form.fields['title'].initial = release['title']
    form.fields['format'].initial = 'Vinyl'
    form.fields['genre'].initial = " ".join(release['genre'])
    form.fields['country'].initial = release['country']
    form.fields['style'].initial = " ".join(release['style'])
    form.fields['label'].initial = release['label'][0]
    return form

# pulls release from discogs api based on catalog number
# and returns dictionary from parsed json
def get_release(cat_number):
    url = "https://api.discogs.com/database/search?q=" \
          + cat_number + "&token=" + DISCOGS_TOKEN
    response = requests.get(url)
    json = response.json()
    release = json['results'][0]
    return release

# saves releases to database
def create_release(request):
    form = ReleaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('collection')
    else:
        print(form.errors)
    return render(request, 'VinylCollection/add_album.html')

# displays all releases in the collection
def collection(request):
    releases = Release.objects.all()
    context = {
        'releases': releases,
    }
    return render(request, 'VinylCollection/collection.html', context)

# displays individual release information
def details(request, pk):
    pk = int(pk)
    release = get_object_or_404(Release, pk=pk)
    context = {
        'release': release
    }
    return render(request, 'VinylCollection/details.html', context)

def get_score(release):
    search_text = release['title']
    page = requests.get()
