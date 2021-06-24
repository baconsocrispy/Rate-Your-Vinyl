from django.shortcuts import render, redirect
from .models import Categorie, Note
from .forms import NoteForm, CategoryForm


def Home(request):
    return render(request, 'NoteTaking/NoteTaking_home.html')

def AddNotes(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('NoteTaking_home')
    else:
        print(form.errors)
        form = NoteForm()

    context = {
        'form': form
    }

    return render(request, 'NoteTaking/NoteTaking_addnotes.html', context)

def AddCategories(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('NoteTaking_home')
    else:
        print(form.errors)
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'NoteTaking/NoteTaking_addcategories.html', context)
