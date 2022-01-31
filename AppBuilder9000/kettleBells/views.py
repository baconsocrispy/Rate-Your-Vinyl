from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from .models import Moves
from .forms import MovesForm


def kettleBells(request):
    return render(request, 'kettleBells/kettleBells_home.html')


def moves(request):
    moves_list = Moves.objects.all()
    return render(request, 'kettleBell_exercises.html', {'moves_list': moves_list})




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