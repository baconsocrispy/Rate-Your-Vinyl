from django.shortcuts import render, redirect
from .forms import CreateForm


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
