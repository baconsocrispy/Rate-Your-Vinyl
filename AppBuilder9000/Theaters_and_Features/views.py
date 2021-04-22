from django.shortcuts import render, redirect
from .forms import TheaterForm

# Create your views here.
def Theater_home(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_home.html')


def new_Theater(request):
    form = TheaterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Theaters_and_Features_home')
        else:
            content = {'form': form}
            return render(request, 'Theaters_and_Features/Theaters_and_Features_add.html', content)
    content = {'form': form}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_add.html', content)




