from django.shortcuts import render, redirect
from .forms import ArtistForm
from .models import *

def home(request):
    return render(request, 'ArtGallery_home.html')

def apply(request):
    form = ArtistForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("ArtGallery_home")
    return render(request, 'ArtGallery_login.html', {'form': form})

def users(request):
    user_display = Artist.Artists.all()
    context = {'user_display': user_display}
    return render(request, 'ArtGallery_users.html', context)


