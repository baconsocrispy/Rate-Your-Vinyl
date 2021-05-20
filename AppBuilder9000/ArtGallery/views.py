from django.shortcuts import render


def artgallery(request):
    return render(request, 'ArtGallery/ArtGallery_home.html')
