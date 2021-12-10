from django.shortcuts import render, redirect
from .forms import PlantsForm
from .models import Plants

# This renders the home page of the gardening app
def gardening_home(request):
    return render(request, "Gardening/gardening_home.html")

# This posts the garden planner form to the database
def create_plant(request):
    if request.method == "POST":
        form = PlantsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("show_plant")
    else:
        form = PlantsForm()
        context = {'form': form}
    return render(request, "Gardening/createPlant_form.html", context)

# This shows what plants are currently in the database
def show_plant(request):
    show_plants = Plants.objects.all()

    context = {'show_plants': show_plants}
    return render(request, "Gardening/show_plant.html", context)
