from django.shortcuts import render, redirect
from .forms import RecipeForm


# render home page
def home(request):
    return render(request, 'Desserts/desserts_home.html')


# render add_recipe page
def add_recipe(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('desserts_home')
    content = {'form': form}
    return render(request, 'Desserts/desserts_add_recipe.html', content)
