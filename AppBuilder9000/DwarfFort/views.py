from django.shortcuts import render, get_object_or_404, redirect
from .models import Fbeast
from .forms import FbeastForm

# Story 1 - Build Basic App
def dfort_home(request):
    return  render(request, 'DwarfFort/dfort_home.html')

# Story 2 - Build Model
def dfort_create(request):
    form = FbeastForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')
    content = {'form': form}
    return  render(request, 'DwarfFort/dfort_create.html', content)