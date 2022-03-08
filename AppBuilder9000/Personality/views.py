from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, ComparedPerson
from .forms import PersonForm


#def personality_home(request):
#    return render(request, 'Personality/personality_home.html')

def personality_home(request):
    form = PersonForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['person']
        return personality_compare(request, pk)
    content = {'form': form}
    return render(request, 'Personality/personality_home.html', content)


#def personality_create(request):
#    return render(request, 'Personality/personality_create.html')

def personality_create(request):
    form = PersonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/Personality/')
    content = {'form': form}
    return render(request, 'Personality/personality_create.html', content)


#def personality_compare(request):
#    return render(request, 'Personality/personality_compare.html')

def personality_compare(request, pk):
    person = get_object_or_404(Person, pk=pk)
    #current_total = person.initial_deposit
    #table_contents = {}

    content = {'person': person}
    return render(request, 'Personality/personality_compare.html', content)
