from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm, JobSearchForm
import requests
import json


def personality_job_api(request):
    return render(request, 'Personality/personality_job_api.html')


def personality_home(request):
    return render(request, 'Personality/personality_home.html')


def personality_create(request):
    form = PersonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../compare')
    content = {'form': form}
    return render(request, 'Personality/personality_create.html', content)


def personality_compare(request):
    person = Person.Persons.all()
    content = {"person": person}
    return render(request, 'Personality/personality_compare.html', content)


def personality_details(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = JobSearchForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            query = form.cleaned_data['query']
            location = form.cleaned_data['location']

            url = "https://indeed12.p.rapidapi.com/jobs/search"
            headers = {
                'x-rapidapi-host': "indeed12.p.rapidapi.com",
                'x-rapidapi-key': "9afece8438msh5f25fff510a60bbp1954d2jsn7f98f53b6d37"
            }
            parameters = {
                "query": query,
                "location": location
            }
            response = requests.request("GET", url, headers=headers, params=parameters)
            job_info = json.loads(response.text)
            job_list = []
            for job in job_info['hits']:
                job_list.append([job['title'], job['company_name'], job['location']])
            content = {'job_list': job_list}
            return render(request, 'Personality/personality_job_api.html', content)
    content = {'person': person, 'form': form}
    return render(request, 'Personality/personality_details.html', content)


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



