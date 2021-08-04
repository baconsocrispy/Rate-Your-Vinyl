from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, "AlbumReviews/AlbumReviews_details.html", context)

def Album_delete(request, id):
    item = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('AlbumReviews_list')
    context = {'item': item}
    return render(request, 'AlbumReviews/AlbumReviews_delete.html', context)

def Album_edit(request, id):
    item = get_object_or_404(Album, id=id)
    form = AlbumForm(data=request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('AlbumReviews_list')
    context = {'form': form}
    return render(request, "AlbumReviews/AlbumReviews_edit.html", context)

