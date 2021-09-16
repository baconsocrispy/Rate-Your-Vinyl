from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExercisesForm
from .models import Exercises

# Create your views here.
def home(request):
    return render(request, 'exercises_home.html', {})


def create(request):
    form = ExercisesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('exercises_create')
    else:
        print(form.errors)
        form = ExercisesForm()
        context = {
            'form': form,
        }
    return render(request, 'exercises_create.html', {'Exercises': Exercises})
