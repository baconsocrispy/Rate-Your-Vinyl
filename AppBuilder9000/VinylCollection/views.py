from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Avg
from django.urls import reverse_lazy
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist
from .pitchfork import *
import datetime

# renders homepage
def home(request):
    return render(request, 'VinylCollection/home.html')

# renders collection page
def collection(request):
    releases = Release.objects.all()
    context = {
        'releases': releases,
    }
    return render(request, 'VinylCollection/collection.html', context)

# renders the scores page
def scores(request):
    releases_with_scores = Release.objects.filter(pf_rating__gt=0).order_by('-pf_rating')
    average_score = releases_with_scores.aggregate(Avg('pf_rating'))
    clean_average = round(average_score['pf_rating__avg'], 1)
    context = {
        'releases': releases_with_scores,
        'average_score': clean_average,
    }
    return render(request, 'VinylCollection/scores.html', context)

# renders individual release pages
def details(request, pk):
    pk = int(pk)
    release = get_object_or_404(Release, pk=pk)
    context = {
        'release': release
    }
    return render(request, 'VinylCollection/details.html', context)

# saves releases to database
def create_release(request):
    form = ReleaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('collection')
    else:
        print(form.errors)
    return render(request, 'VinylCollection/collection.html')

# renders update page
class ReleaseUpdateView(UpdateView):
    model = Release
    fields = '__all__'
    success_url = reverse_lazy('collection')

# renders delete page
class ReleaseDeleteView(DeleteView):
    model = Release
    success_url = reverse_lazy('collection')

# -------- DISCOGS API LOGIC BELOW ----------v

# my user token to access discogs API
DISCOGS_TOKEN = "DBiUmQgyHHBGmXsybviPrgmVVSJmMDdhpxBAGwle"

# -gathers catalog number from user input on homepage catalog widget
# -displays release info from discogs/pitchfork to ensure it's correct
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

# -pulls release from discogs api based on catalog number
# -returns dictionary from parsed json
def get_release(cat_number):
    url = "https://api.discogs.com/database/search?q=" \
          + cat_number + "&token=" + DISCOGS_TOKEN
    response = requests.get(url)
    json = response.json()
    release = json['results'][0]
    return release

# auto-populates release form with data pulled from discogs api/pitchfork
def populate_form(release, blank_form):
    form = blank_form
    form.fields['title'].initial = release['title']
    form.fields['format'].initial = 'Vinyl'
    form.fields['genre'].initial = ", ".join(release['genre'])
    form.fields['release_date'].initial = datetime.date(int(release['year']), 1, 1)
    form.fields['country'].initial = release['country']
    form.fields['style'].initial = ", ".join(release['style'])
    form.fields['label'].initial = release['label'][0]
    form.fields['pf_rating'].initial = get_score(release)
    form.fields['cover_image'].initial = release['cover_image']
    return form