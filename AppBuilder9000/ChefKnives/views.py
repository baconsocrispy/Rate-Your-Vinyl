import requests
from django.shortcuts import render, redirect
from .forms import KnifeForm
from .models import ChefKnives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'ChefKnives/ChefKnives_Home.html')


def chefknives_view(request):
    view = ChefKnives.objects.all()
    return render(request, 'ChefKnives/ChefKnives_View.html', {'view': view})


def chefknives_create(request):
    form = KnifeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ChefKnives_Create')
        else:
            print(form.errors)
            form = KnifeForm()
    context = {'form': form}
    return render(request, 'ChefKnives/ChefKnives_Create.html', context)
