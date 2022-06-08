from django.shortcuts import render, redirect, get_object_or_404
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

def saveEdit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Jobs, pk=pk)
    form = JobsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            jobs = Jobs.objects.all()
            form2 = form.save(commit=False)
            form2.save()
            return render(request, 'JobScraping/JobScraping_history.html', {'jobs': jobs})
        else:
            print(form.errors)
    else:
        return render(request, 'JobScraping/JobScraping_history.html')

def JobScraping_details(request, pk):
    pk = int(pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    context = {'job': jobs}
    return render(request, 'JobScraping/JobScraping_details.html', context)

def JobScraping_editJob(request, pk):
    pk = int(pk)
    item = get_object_or_404(Jobs, pk=pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    form = JobsForm(data=request.POST or None, instance=item)
    context = {
        'form': form,
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_editJob.html', context)
