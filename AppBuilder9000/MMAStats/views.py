from django.shortcuts import render
from .forms import ChampForm

def MMAHome(request):
    return render(request, 'MMA_home.html')

def MMACreate(request):
    context = {}
    form = ChampForm (request.POST or None, request.FILES or None)

    # if form data is valid
    if form.is_valid():
        # save form data to our model
        form.save()

    context['form']= form
    return render(request, "MMA_create.html", context)
