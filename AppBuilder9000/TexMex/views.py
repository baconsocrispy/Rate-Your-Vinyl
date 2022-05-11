from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import FoodForm
from .models import Food


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def texmex_home(request):
    return render(request, 'TexMex/texmex_home.html')
# Create your views here.


def edit_recipe(request):
    foods = Food.objects.all()
    return render(request, 'TexMex/recipe_page.html', {'foods': foods})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    form = FoodForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('edit_recipe')
        else:
            print(form.errors)
    else:
        return render(request, 'TexMex/present_food.html', {'form':form})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('edit_recipe')
    context = {"item": item,}
    return render(request,"TexMex/confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        #creates form instance and binds data to it
        form = FoodForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('edit_recipe')
    else:
        return redirect('edit_recipe')

def createRecord(request):
    form = FoodForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('edit_recipe')
    else:
        print(form.errors)
        form = FoodForm()
    context = {
        'form': form,
    }
    return render(request, "TexMex/createRecord.html", context)
