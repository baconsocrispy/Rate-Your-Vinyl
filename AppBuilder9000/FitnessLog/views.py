from django.shortcuts import render, redirect
from .forms import EntryForm
from django.http import HttpResponse
from .models import Entry


# user story 1
def fitness_home(request):
    return render(request, 'FitnessLog/fitness_home.html')


# user story 2: Create and entry
def create_entry(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fitness_home')
    content = {'form': form}
    return render(request, 'FitnessLog/fitness_entry_create.html', content)


# user story 3: Display all items from the database
def fitness_read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'FitnessLog/fitness_read.html', content)
