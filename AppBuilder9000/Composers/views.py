from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .forms import ComposerForm
from .models import Composer


# Create your views here.
def composers(request):
    return render(request, 'composers/composers_home.html')


def create_composer(request):
    form = ComposerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_home')
    content = {'form': form}
    return render(request, 'composers/composers_create.html', content)

def composers_details(request,pk):
    details = get_object_or_404(Composer, pk=pk)
    context = {'details': details}
    return render(request, 'Composers/composers_details.html', context)
