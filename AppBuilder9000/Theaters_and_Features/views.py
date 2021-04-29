from django.shortcuts import render, redirect
from .forms import TheaterForm
from .models import Theaters
# Create your views here.



def Theater_home(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_home.html')


def new_Theater(request):
    form = TheaterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('new_Theater')
    # else:
        # print(form.errors)
        # form = TheaterForm()
    context = {'form': form}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_add.html', context)


def find_Theater(request):
    all_theaters = Theaters.objects.all
    context = {'all_theaters': all_theaters}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_find.html', context)


def Theater_details(request, pk):
    pk = int(pk)
    get_theaters = Theaters.objects.filter(pk=pk)
    context = {'get_theaters': get_theaters}
    return render(request, 'Theaters_and_Features/Theaters_and_Features_detail.html', context)






