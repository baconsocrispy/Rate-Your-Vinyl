from django.shortcuts import render, get_object_or_404, redirect

from MoveState.form import movestateForm
from MoveState.models import Movestate


def movestate_home(request):
    return render(request, "MoveState/movestate_home.html")


def add_state(request):
    form = movestateForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movestate_home')
    else:
        print(form.errors)
        form = movestateForm()
    context = {
        'form': form,
    }
    return render(request, 'MoveState/add_state.html', context)


def list_state(request):
    list = Movestate.Movers.all()
    return render(request, 'MoveState/list_state.html', {'list': list})

def movestate_details(request, pk):
    details = get_object_or_404(Movestate, pk=pk)
    return render(request, 'Movestate/movestate_details.html', {'details': details})
