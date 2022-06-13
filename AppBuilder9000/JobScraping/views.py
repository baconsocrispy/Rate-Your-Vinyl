from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobsForm
from .models import Jobs
from bs4 import BeautifulSoup
import requests
import json

# This view takes the user to the home page
def JobScraping_home(request):

    # Gets the request of the data from the website.
    page = requests.get('https://forecast.weather.gov/MapClick.php?lat=45.5118&lon=-122.6756#.YqN-yXbMIuU')
    soup = BeautifulSoup(page.content, 'html.parser')
    today = soup.select('li.forecast-tombstone:first-child')

    # We will be extracting the current day's weather only.
    current = today[0].find(class_='period-name').get_text()
    description = today[0].find(class_='short-desc').get_text()
    temp = today[0].find(class_='temp-high').get_text()

    data = [current, description, temp]
    context = {'data': data}
    return render(request, 'jobScraping/JobScraping_home.html', context)


# This view takes the user to the API job search page
def searchAPI(request):
    return render(request, 'JobScraping/APIJobSearch.html')


# This view sends the data input by the user an initiates the API request and returns APIJobSearch.html with the
# returned values from the API response
def searchResults(request):
    # This gets the location information submitted with the form on APIJobSearch.html
    description = request.POST['what']
    # This changes the string received from the form to a syntax that the url can recognize (e.g. exchange " " for %20)
    formattedDescription = (description.replace(" ", "%20")).replace(",", "%2C")
    # This gets the location information submitted with the form on APIJobSearch.html
    location = request.POST['location']
    # This changes the string received from the form to a syntax that the url can recognize (e.g. exchange " " for %20)
    formattedLocation = (location.replace(" ", "%20")).replace(",", "%2C")

    # creates an array that will be sent to the page as context so that the search bars will maintain their data when
    # the page is re-loaded
    search = [description, location]

    # Queries an API for 20 results based on the location and description received above
    response = requests.get('https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=41b593cb&app_key=58bb774dace8a185a8cc32fbdff00416&results_per_page=20&what={}&where={}&sort_by=date'.format(formattedDescription, formattedLocation))

    # pulls the json data from the API response
    json_data = response.json()
    # json_data is a dictionary with a single key which contains an array of the job objects. This sets the variable
    # results to that array.
    results = json_data['results']

    jobs = []
    for job in results:
        try:
            jobs.append([job['title'], job['company']['display_name'], job['created'], job['redirect_url'], job['salary_min'], job['salary_max']])
        except:
            jobs.append([job['title'], job['company']['display_name'], job['created'], job['redirect_url'], '', ''])


    # TEST ==========================

    print('################')
    print('')
    print('################')

    # TEST ==========================

    return render(request, 'JobScraping/APIJobSearch.html', {'jobs': jobs, 'search': search})


# This view takes the user to the JobScraping_input.html page where they can input job data into a form
def JobScraping_input(request):
    form = JobsForm(request.POST or None)
    context = {'form': form}
    return render(request, 'JobScraping/JobScraping_input.html', context)


# This view is activated from JobScraping_input.html, and saves any data that was in the form to the database.
def inputJob(request):
    # This line creates a form element and binds data to it
    form = JobsForm(request.POST or None)
    # This check if the data in the form are valid, and if they are it saves them and returns the user to the homepage
    if form.is_valid():
        form.save()
        return redirect('JobScraping_home')
    else:
        # If the form data are not valid the respective errors are printed
        print(form.errors)
        # the form variable is reset to represent the base JobsForm() object
        form = JobsForm()
    context = {
        'form': form,
    }
    return render(request, 'JobScraping/JobScraping_input.html', context)


# This view requests all the information in the database and sends it as context to JobScraping_history.html and then
# renders that html page.
def JobScraping_history(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_history.html', context)


# This view saves the changes made to a form on JobScraping_editJob.html
def saveEdit(request, pk):
    # converts the argument pk (which is a string) to an integer
    pk = int(pk)
    # This line gets the item with the requested primary key from the database
    item = get_object_or_404(Jobs, pk=pk)
    # Again, creates a form objects and binds data to it
    form = JobsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            # this creates a new jobs object of all the database so this if statement can redirect you to the hist page.
            jobs = Jobs.objects.all()
            form2 = form.save(commit=False)
            form2.save()
            return render(request, 'JobScraping/JobScraping_history.html', {'jobs': jobs})
        else:
            print(form.errors)
    else:
        return render(request, 'JobScraping/JobScraping_history.html')


# This view is a two-part view. If the request sent to this view is in POST it will delete the db item with the
# respective pk. If the request sent to this view is in GET it will send the user to a page that will ask them to
# confirm the choice to delete. When they confirm the request is sent back to this view again this time as POST.
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Jobs, pk=pk)
    # if POST then delete
    if request.method == 'POST':
        item.delete()
        return redirect('JobScraping_history')
    # if anything other than POST check if they really want ot delete
    context = {'item': item,}
    return render(request, 'JobScraping/JobScraping_confirmDelete.html', context)


# This view loads the JobScraping_details.html which shows the data for a single job
def JobScraping_details(request, pk):
    # Changes pk from string to int
    pk = int(pk)
    # Gets the specific job data from the database by using the primary key (pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    # Creates an object with the data that can be sent to the html file
    context = {'job': jobs}
    print(context)
    # Renders the html file and sends the data to it in the variable 'context'
    return render(request, 'JobScraping/JobScraping_details.html', context)


# This view loads the editJob.html and passes it information so that it can display a form with the current data
# (which uses {'form': form},) and also save that form to the database with (which uses {'jobs': jobs},)
def JobScraping_editJob(request, pk):
    pk = int(pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    form = JobsForm(data=request.POST or None, instance=jobs)
    context = {
        'form': form,
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_editJob.html', context)