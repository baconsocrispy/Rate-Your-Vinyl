from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlacesForm


def seattle_home(request):
    return render(request, 'Seattle/seattle_home.html')


def seattle_create(request):
    form = PlacesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('seattle_home')
    content = {'form': form}
    return render(request, 'Seattle/seattle_create.html', content)
