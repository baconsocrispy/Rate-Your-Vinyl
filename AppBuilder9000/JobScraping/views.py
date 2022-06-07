from django.shortcuts import render, redirect
from .forms import JobsForm
from .models import Jobs

# Create your views here.
def JobScraping_home(request):
    return render(request, 'jobScraping/JobScraping_home.html')

def JobScraping_input(request):
    form = JobsForm(request.POST or None)
    context = {'form': form}
    return render(request, 'JobScraping/JobScraping_input.html', context)

def JobScraping_history(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_history.html', context)

def inputJob(request):
    form = JobsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('JobScraping_home')
    else:
        print(form.errors)
        form = JobsForm()
    context = {
        'form': form,
    }
    return render(request, 'JobScraping/JobScraping_input.html', context)
