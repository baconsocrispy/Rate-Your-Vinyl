from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, ComparedPerson, SelectPerson
from .forms import PersonForm, SelectPersonForm
from django.views import generic
from django.http import HttpResponse
import requests
import json


#def personality_home(request):
#    return render(request, 'Personality/personality_home.html')

def personality_home(request):
    return render(request, 'Personality/personality_home.html')


#def personality_create(request):
#    return render(request, 'Personality/personality_create.html')

def personality_create(request):
    form = PersonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../compare')
    content = {'form': form}
    return render(request, 'Personality/personality_create.html', content)


#def personality_compare(request):
#    return render(request, 'Personality/personality_compare.html')

def personality_compare(request):
    data = Person.Persons.all()
    pers = {"person": data}

#    content = {'person': person}
    return render(request, 'Personality/personality_compare.html', pers)


#class PersonalityDetailView(generic.DetailView):
#    print("details")
#    pers = Person.Persons.all()
#    form = PersonForm(data=pers or None)
#    model = Person
#    template_name = 'Personality/personality_details.html'

def personality_details(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'Personality/personality_details.html', {'person': person})


def personality_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(data=request.POST or None, instance=person)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../compare')
    content = {'person': person, 'form': form}
    return render(request, 'Personality/personality_edit.html', content)


def personality_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(data=request.POST or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('../../compare')
    content = {'person': person, 'form': form}
    return render(request, 'Personality/personality_delete.html', content)



