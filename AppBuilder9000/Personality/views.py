from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm, JobSearchForm
import requests
import json
from bs4 import BeautifulSoup


def personality_job_api(request):
    return render(request, 'Personality/personality_job_api.html')


def personality_trait_info(request):
    page = requests.get("https://en.wikipedia.org/wiki/Big_Five_personality_traits")
    soup = BeautifulSoup(page.content, 'html.parser')
    # Scraping general information about the traits
    info = soup.find_all('p')[0].get_text() + soup.find_all('p')[2].get_text()
    openness = soup.find_all('p')[7].get_text()
    conscientiousness = soup.find_all('p')[9].get_text()
    extraversion = soup.find_all('p')[10].get_text() + soup.find_all('p')[11].get_text() + soup.find_all('p')[12].get_text()
    agreeableness = soup.find_all('p')[13].get_text() + soup.find_all('p')[14].get_text() + soup.find_all('p')[15].get_text() + soup.find_all('p')[16].get_text()
    neuroticism = soup.find_all('p')[17].get_text() + soup.find_all('p')[18].get_text() + soup.find_all('p')[19].get_text()
    print(info)
    print(openness)
    print(conscientiousness)
    print(extraversion)
    print(agreeableness)
    print(neuroticism)
    content = {'info': info, 'openness': openness, 'conscientiousness': conscientiousness, 'extraversion': extraversion, 'agreeableness': agreeableness, 'neuroticism': neuroticism}
    return render(request, 'Personality/personality_trait_info.html', content)


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
            job_url = job_info['indeed_final_url']
            job_list = []
            for job in job_info['hits']:
                job_list.append([job['title'], job['company_name'], job['location']])
            content = {'job_list': job_list, 'job_url': job_url}
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



