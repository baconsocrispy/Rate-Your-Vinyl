from django.shortcuts import get_object_or_404, redirect, render

from .forms import Trails_Form
from .models import AtvTrails


# this will return to the home page
def Atv_home(request):
    return render(request, 'AtvTrails_home.html')


def add_trail(request):
    form = Trails_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Atv_home')
    else:
        print(form.errors)
        form = Trails_Form
        context = {'form': form}
    return render(request, 'AtvTrails_create.html', context)


def list_trails(request):
    trails = AtvTrails.objects.all()
    return render(request, 'AtvTrails_list.html', {'trails': trails})


def trail_details(request, pk):
    details = get_object_or_404(AtvTrails, pk=pk)
    context = {'details': details}
    return render(request, 'AtvTrails_details.html', context)


def trail_edit(request, pk):
    show_trail = get_object_or_404(AtvTrails, pk=pk)
    form = Trails_Form(data=request.POST or None,
                       instance=show_trail)  # this instance makes it show the info that was already entered in about the pokemon you are editing
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('trail_details', pk)
    context = {'form': form}
    return render(request, 'AtvTrails_edit.html', context)


def trail_delete(request, pk):
    show_trail = get_object_or_404(AtvTrails, pk=pk)
    form = Trails_Form(data=request.POST or None, instance=show_trail)
    if request.method == 'POST':
        show_trail.delete()
        return redirect('list_trails')
    return render(request, 'AtvTrails_delete.html', {'show_trail': show_trail, 'form': form})
