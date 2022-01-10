from django.shortcuts import render, redirect, get_object_or_404
import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import choose
import requests
import json

def hiphop_home(request):
    # this will return user to hip hop home page
    return render(request, 'Hiphop/hiphop_home.html')

def createChoose(request):
    form = ChooseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('hiphop_home')
    else:
        print(form.errors)
        form = ChooseForm()
    context = {
        'form': form,
    }
    return render(request, 'Hiphop/hiphop_create.html', context)


def choose_view(request):
    choose = choose.objects.all()
    return render(request, 'hiphop_view.html', {'choose': choose})