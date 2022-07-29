from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Avg
from django.urls import reverse_lazy
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist
from bs4 import BeautifulSoup
import requests


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

# gathers vinyl catalog number from user
def add_album(request):
    return render(request, 'VinylCollection/add_album.html')

# displays release info from discogs/pitchfork to ensure it's correct
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

# auto-populates release form with data pulled from discogs api/pitchfork
def populate_form(release, blank_form):
    form = blank_form
    form.fields['title'].initial = release['title']
    form.fields['format'].initial = 'Vinyl'
    form.fields['genre'].initial = ", ".join(release['genre'])
    form.fields['country'].initial = release['country']
    form.fields['style'].initial = ", ".join(release['style'])
    form.fields['label'].initial = release['label'][0]
    form.fields['pf_rating'].initial = get_score(release)
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

def display_scores(request):
    releases_with_scores = Release.objects.filter(pf_rating__gt=0).order_by('-pf_rating')
    average_score = releases_with_scores.aggregate(Avg('pf_rating'))
    context = {
        'releases': releases_with_scores,
        'average_score': average_score,
    }
    return render(request, 'VinylCollection/scores.html', context)

# displays individual release information
def details(request, pk):
    pk = int(pk)
    release = get_object_or_404(Release, pk=pk)
    context = {
        'release': release
    }
    return render(request, 'VinylCollection/details.html', context)

# ---v--- PITCHFORK SCRAPING LOGIC BELOW ---v---

# gets the review page, soupifies the response,
# extracts elements that contain the score,
# returns the score if one is found
def get_score(release):
    page = get_pitchfork_review_page(release)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find('p') # score sometimes in the first 'p' element
    span = soup.find('span', {'class': 'score'}) # score sometimes in span element named 'score'
    score = test_elements_for_score(p, span)
    print(p) # included for Story 6 criteria
    print(span) # included for Story 6 criteria
    return score

# checks if the scrape actually pulled a score and,
# if so, returns it.
def test_elements_for_score(p, span):
    if span:
        try:
            return float(span.text)
        except:
            print('span is not a valid score')
    try:
        return float(p.text)
    except:
        print('p is not a valid score')

# compiles the elements of a pitchfork review url
def get_pitchfork_review_page(release):
    release_text = clean_string(release['title'])
    url = "https://pitchfork.com/reviews/albums/" + release_text
    return requests.get(url)

# formats title string for pitchfork review url
def clean_string(string):
    word_list = string.split()
    new_list = []
    for word in word_list:
        clean_word = "".join(filter(str.isalnum, word))
        if clean_word:
            new_list += [clean_word]
    clean_str = "-".join(new_list)
    return clean_str.lower()