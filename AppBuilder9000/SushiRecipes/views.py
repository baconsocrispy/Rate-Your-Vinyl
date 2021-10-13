from django.shortcuts import render, redirect, get_object_or_404
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


def sushi_recipes_details(request, pk):
    details = get_object_or_404(SushiRecipes, pk=pk)
    context = {'details': details}
    return render(request, "SushiRecipes/Sushi_Recipes_Details.html", context)
