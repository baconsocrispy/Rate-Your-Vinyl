from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Render home page
def AlbumReviews_home(request):
    return render(request, "AlbumReviews/AlbumReviews_home.html")

def AlbumReviews_add(request):
    form = AlbumForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('AlbumReviews_list')
    return render(request, "AlbumReviews/AlbumReviews_add.html", {'form': form})

def AlbumReviews_list(request):
    albums = Album.objects.order_by('-id')
    context = {'albums': albums}
    return render(request, "AlbumReviews/AlbumReviews_list.html", context)

def Album_details(request, id):
    details = Album.objects.get(id=id)
    context = {'details': details}
    return render(request, "AlbumReviews/Albumreviews_details.html", context)