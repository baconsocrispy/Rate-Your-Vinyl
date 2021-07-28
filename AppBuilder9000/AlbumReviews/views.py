from django.shortcuts import render
from .forms import AlbumForm
from .models import Album

# Render home page
def home(request):
    return render(request, "AlbumReviews/AlbumReviews_home.html")
