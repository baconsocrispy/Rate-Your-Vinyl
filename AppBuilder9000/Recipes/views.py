from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.
def Recipes_Home(request):
    return render(request, 'Recipes_Home.html')

def Recipes_Create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Recipes_Create')
    else:
        print(form.errors)
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'Recipes_Create.html', context)

def Recipes_See(request):
    recipes = Recipe.objects.all()
    return render(request, 'Recipes_See.html', {'recipes': recipes})

def Recipes_Details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Recipes_See')
        else:
            print(form.errors)
    else:
        return render(request, 'Recipes_Details.html', {'form': form})


def Recipes_Edit(request, pk):
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Recipes_See')
    context = {'form': form}
    return render(request, 'Recipes_Edit.html', context)

def Recipes_Delete(request, pk):
    item = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('Recipes_See')
    context = {'item': item, 'form': form}
    return render(request, 'Recipes_Delete.html', context)

