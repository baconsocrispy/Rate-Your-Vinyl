from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkoutEquipment
from django.shortcuts import render
from .forms import WorkoutEquipmentForm


# function to render Homepage
def workout_equipment_home(request):
    return render(request, "WorkoutEquipment/WorkoutEquipHome.html")

#
def workout_equip_console(request):
    # if POST request type then process the forms data
    form = WorkoutEquipmentForm(request.POST or None)
    # checking if the form is valid
    if form.is_valid():
        form.save()
        return redirect('WorkoutEquipHome')
    else:
        print(form.errors)   # create empty form if not filled out correctly
        form = WorkoutEquipmentForm()
    context = {
        'form': form    # context form object
    }   # pass in request object, pass in file, and pass in context variables to be returned
    return render(request, 'WorkoutEquipment/WorkoutEquipConsole.html', context)

def workout_equip_create(request):
    form = WorkoutEquipmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('workout_equip_console')
    else:
        print(form.errors)
        form = WorkoutEquipmentForm()
    context = {
        'form': form,
    }
    return render(request, 'WorkoutEquipment/WorkoutEquipCreate.html', context)

# Accidentally jumped the gun on this details view function,  it isn't functional yet but will be when that user
# story comes up.
# I realize now this is not proper work practice so will make sure to hold off on additional functions that don't relate
# to the current user story


def workout_equip_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(WorkoutEquipment, pk=pk)
    form = WorkoutEquipmentForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('WorkoutEquipConsole')
        else:
            print(form.errors)
    else:
        return render(request, 'WorkoutEquipment/PresentWorkoutEquip.html', {'form': form})





