from django.shortcuts import render


def home(request):
    return render(request, 'ArtGallery_home.html')
