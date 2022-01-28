from django.shortcuts import render, redirect
from .models import Moves
from .forms import MovesForm


def kettleBells(request):
    return render(request, 'kettleBells/kettleBells_home.html')


def moves(request):
    return render(request, 'exercises.html')


def add_exercise(request):
    form = MovesForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('KB_home')
    else:
        print(form.errors)
        form = MovesForm()
    context = {
        'form': form,
    }
    return render(request, 'kettleBells/kettleBells_add.html', context)