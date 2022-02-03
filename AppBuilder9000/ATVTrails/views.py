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
