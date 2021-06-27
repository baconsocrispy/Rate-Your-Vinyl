from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie, Note
from .forms import NoteForm, CategoryForm


def Home(request):
    notes = Note.object.all()
    return render(request, 'NoteTaking/NoteTaking_home.html', { 'notes': notes })

def Details(request, pk):
    pk = int(pk)
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(data=request.POST or None, instance=note)

    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('NoteTaking_home')
        else:
            print(form.errors)
    else:
        return render(request, 'NoteTaking/NoteTaking_details.html', { 'form': form })

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

def DeleteNotes(request, pk):
    pk = int(pk)
    item = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('NoteTaking_home')

    context = { "item": item }
    return render(request, 'NoteTaking/NoteTaking_confirmdelete.html', context)

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
