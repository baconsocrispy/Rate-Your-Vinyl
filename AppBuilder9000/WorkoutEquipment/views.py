from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkoutEquipment
from .forms import WorkoutEquipmentForm


# function to render Homepage
def workout_equipment_home(request):
    products = WorkoutEquipment.objects.all()
    return render(request, "WorkoutEquipment/WorkoutEquipHome.html", {'products': products})


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


def workout_equip_display(request):
    display_items = WorkoutEquipment.objects.all()
    content = {'display_items': display_items}
    return render(request, 'WorkoutEquipment/WorkoutEquipDisplay.html', content)


def workout_equip_details(request, pk):
    details = get_object_or_404(WorkoutEquipment, pk=pk)
    content = {'details': details}
    return render(request, 'WorkoutEquipment/WorkoutEquipDetails.html', content)


def workout_equip_edit(request, pk):
    edit = get_object_or_404(WorkoutEquipment, pk=pk)
    form = WorkoutEquipmentForm(data=request.POST or None, instance=edit)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('workout_equip_console')
        else:
            print(form.errors)
            form = WorkoutEquipmentForm()
    context = {
        'form': form, 'edit': edit
    }
    return render(request, 'WorkoutEquipment/WorkoutEquipEdit.html', context)


def workout_equip_delete(request, pk):
    item = get_object_or_404(WorkoutEquipment, pk=pk)
    form = WorkoutEquipmentForm (data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('workout_equip_display')
    return render(request, 'WorkoutEquipment/WorkoutEquipDelete.html', {'item': item, 'form': form})

def confirmed(request):
    if request.method == 'POST':
        # created form instance and binds data to it
        form = WorkoutEquipmentForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('workout_equip_console')
    else:
        return redirect('workout_equip_console')





