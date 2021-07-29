from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Render home page
def home(request):
    return render(request, "AlbumReviews/AlbumReviews_home.html")

def add(request):
    form = AlbumForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('AlbumReviews_add')
    return render(request, "AlbumReviews/AlbumReviews_add.html", {'form': form})
