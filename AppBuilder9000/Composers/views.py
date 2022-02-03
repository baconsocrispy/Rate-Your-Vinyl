from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .forms import ComposerForm
from .models import Composer


# Create your views here.
def composers(request):
    return render(request, 'Composers/composers_home.html')


def create_composer(request):
    form = ComposerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_home')
    content = {'form': form}
    return render(request, 'Composers/composers_create.html', content)


def composers_list(request):
    composer_list = Composer.Composers.all()
    context = {'composer_list': composer_list}
    return render(request, 'Composers/composers_list.html', context)


def composers_details(request, pk):
    details = get_object_or_404(Composer, pk=pk)
    context = {'details': details}
    return render(request, 'Composers/composers_details.html', context)


def composers_edit(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Composers/composers_list')
        context = {'form': form}
        return render(request, 'Composers/composers_edit.html', context)

def composers_delete(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            item.delete()
            return redirect('composers_list')
        context =({'item':item, 'form':form})
        return render(request, 'Composers/composers_delete.html', context)