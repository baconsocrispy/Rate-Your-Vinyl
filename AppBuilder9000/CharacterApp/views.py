from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


# Create your views here.
def Character_home(request):
    return render(request, "Character_home.html")


def Character_add(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #google.com is a placeholder for the viewing file for the objects
            return redirect('https://google.com')
        else:
            content = {'form': form}
            return render(request, 'Character_add.html', content)
    content = {'form': form}
    return render(request, 'Character_add.html', content)


def Character_success(request):
    return render(request,Character_success.html)