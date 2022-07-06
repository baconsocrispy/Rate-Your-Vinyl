from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Fbeast
from .forms import FbeastForm

# Story 1 - Build Basic App
def dfort_home(request):
    return  render(request, 'DwarfFort/dfort_home.html')

# Story 2 - Build Model
def dfort_create(request):
    form = FbeastForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')
    context = {'form': form}
    return  render(request, 'DwarfFort/dfort_create.html', context)

# Story 3 - Display Database

def dfort_display(request):
    beast = Fbeast.Fbeasts.all().order_by("title")

    # builds collection of models from beast and limits display to 5 at a time
    paginator = Paginator(beast, 5)
    page = request.GET.get('page')
    beastpage = paginator.get_page(page)


    context = {'beastpage' : beastpage}

    return render(request, 'DwarfFort/dfort_display.html', context)

# Display search results

def dfort_search(request):
    if request.method == "POST":
        name = request.POST.get('usr_query')
        beast = Fbeast.Fbeasts.filter(name=name)

        context = { 'name' : name, 'beast' : beast}
        return render(request, 'DwarfFort/dfort_search.html', context)

