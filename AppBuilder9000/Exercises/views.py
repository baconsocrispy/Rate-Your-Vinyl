from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExercisesForm
from .models import Exercises



# Create your views here.
def exercises_home(request):
    return render(request, 'exercises_home.html', {})


def exercises_names(request):
    names = Exercises.objects.all()
    return render(request, 'exercises_names.html', {'names': names})


def exercises_details(request, pk):
    details = get_object_or_404(Exercises, pk=pk)
    context = {'details': details}
    return render(request, 'exercises_details.html', context)


def exercises_create(request):
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
    return render(request, 'exercises_create.html', context)







