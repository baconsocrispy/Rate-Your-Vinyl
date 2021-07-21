from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import NovelForm


def home(request):
    return render(request, "Novels/Novels_home.html")


def novelEntry(request):
    form = NovelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Novels_create')
    context = {'form': form, }
    return render(request, 'Novels/Novels_create.html', context)
