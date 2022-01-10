import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Choice
from .forms import ChooseForm

def hiphop_home(request):
    # this will return user to hip hop home page
    return render(request, 'Hiphop/hiphop_home.html')

def create_choose(request):
    form = ChooseForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('hiphop_home')
    context = {'form': form}
    return render(request, 'Hiphop/hiphop_create.html', context)


#def choose_view(request):
 #   choose = choose.objects.all()
  #  return render(request, 'hiphop_view.html', {'choose': choose})