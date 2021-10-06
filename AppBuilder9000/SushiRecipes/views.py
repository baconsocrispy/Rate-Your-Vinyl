from django.shortcuts import render
from .forms import SushiForm


def sushi_recipes_home(request):
    return render(request, 'SushiRecipes/Sushi_Recipes_Home.html')


def sushi_view(request):
    context = {}
    form = SushiForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "Sushi_View", context)
