from django.shortcuts import render, redirect
from .forms import EntryForm
from django.http import HttpResponse


# user story 1
def fitness_home(request):
    return render(request, 'FitnessLog/fitness_home.html')


# user story 2
def create_entry(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fitness_home')
    content = {'form': form}
    return render(request, 'FitnessLog/fitness_entry_create.html', content)
