from django.shortcuts import render, redirect
from .forms import SushiForm
from .models import SushiRecipes


def sushi_recipes_home(request):
    return render(request, 'SushiRecipes/Sushi_Recipes_Home.html')


def sushi_recipes_view(request):
    view = SushiRecipes.objects.all()
    return render(request, 'SushiRecipes/Sushi_Recipes_View.html', {'view': view})


def sushi_recipes_create(request):
    form = SushiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Sushi_Recipes_Create')
    else:
        print(form.errors)
        form = SushiForm()
        context = {'form': form}
    return render(request, 'SushiRecipes/Sushi_Recipes_Create.html', context)
