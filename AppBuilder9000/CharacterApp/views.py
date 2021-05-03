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
            # google.com is a placeholder for the viewing file for the objects
            return redirect(Character_list)
        else:
            content = {'form': form}
            return render(request, 'Character_add.html', content)
    content = {'form': form}
    return render(request, 'Character_add.html', content)


def Character_list(request):
    Character_all = Character_create.objects.all()
    context = {'Character_all': Character_all}
    return render(request, 'Character_view.html', context)


def CharacterDetails(request, pk):
    pk = int(pk)
    Character_get = Character_create.objects.filter(pk=pk)
    context = {'Character_get': Character_get}
    return render(request, "Character_details.html", context)