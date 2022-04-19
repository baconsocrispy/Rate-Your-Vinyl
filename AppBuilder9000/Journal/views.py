from django.shortcuts import render, redirect,  get_object_or_404
from .models import Entry
from .forms import EntryForm


def journal_home(request):
    return render(request, 'Journal/journal_home.html')


def journal_create(request):
    #branch
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Journal/journal_create.html', content)


def journal_read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'Journal/journal_read.html', content)


def journal_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Journal/journal_update.html', content)


def journal_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'Journal/journal_delete.html', content)