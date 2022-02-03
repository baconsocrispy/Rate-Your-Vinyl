from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateForm
from .models import Turtles


def turtles_home(request):
    return render(request, 'Turtles/turtles_home.html')


def turtles_create(request):
    form = CreateForm(data=request.POST or None)
    # If POST request, process form data.
    if request.method == 'POST':
        # Checks whether it is valid.
        if form.is_valid():
            form.save()
            return redirect('turtles_home')
    content = {'form': form}
    return render(request, 'Turtles/turtles_create.html', content)


def turtles_display(request):
    item = Turtles.Turtles.all()
    context = {'item': item}

    return render(request, 'Turtles/turtles_display.html', context)


# Query database for all data on a certain 'key' from the 'Turtles' class.
def turtles_details(request, pk):
    details = get_object_or_404(Turtles, pk=pk)
    context = {'details': details}

    return render(request, 'Turtles/turtles_details.html', context)
