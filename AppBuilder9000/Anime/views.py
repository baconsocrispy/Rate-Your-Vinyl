from django.shortcuts import render, redirect
from .models import Description
from .forms import DescriptionForm


def anime_home(request):
    descriptions = Description.objects.all()
    return render(request, 'Anime/Anime_index.html', {'descriptions': descriptions})


def Anime_create(request):
    form = DescriptionForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('Add_Anime')
    else:
        return render(request, 'Anime/Anime_create.html', {'form': form})


def Anime_entries(request):
    entries = Description.objects.all()
    return render(request, 'Anime/Anime_entries.html', {'entries': entries})


def Anime_details(request, pk):
    details = Description.get(pk=pk)
    return render(request, "Anime/Anime_details.html", {'details': details})



