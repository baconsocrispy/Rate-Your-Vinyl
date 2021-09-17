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
    pk = int(pk)
    item = get_object_or_404(Exercises, pk=pk)
    form = ExercisesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('exercises_names')
        else:
            print(form.errors)
    else:
        return render(request, 'exercises_names.html', {'form': form})

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







