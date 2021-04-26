from django.shortcuts import render, redirect
from .forms import TheaterForm

# Create your views here.
def Theater_home(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_home.html')


def new_Theater(request):
    form = TheaterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('new_Theater')
    #else:
        #print(form.errors)
        #form = TheaterForm()
    context = {'form': form,}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_add.html', context)


def find_Theater(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_find.html')





