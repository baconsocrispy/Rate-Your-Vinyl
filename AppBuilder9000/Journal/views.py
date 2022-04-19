from django.shortcuts import render, redirect,  get_object_or_404
from .models import Entry
from .forms import EntryForm


def home(request):
    return render(request, 'MyJournal/home.html')


def create(request):
    #branch
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'MyJournal/create.html', content)


def read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'MyJournal/read.html', content)


def update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'MyJournal/update.html', content)


def delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'MyJournal/delete.html', content)