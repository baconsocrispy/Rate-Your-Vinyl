from django.shortcuts import render, redirect
from .forms import ChampForm

def MMAHome(request):
    return render(request, 'MMAStats/MMA_home.html')

def MMACreate(request):
    form = ChampForm (data=request.POST or None)
    # if form data is valid
    if form.is_valid():
        # save form data to our model
        form.save()
        return redirect('MMA_Create')

    context = {'form': form}
    return render(request, "MMAStats/MMA_create.html", context)
