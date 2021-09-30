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