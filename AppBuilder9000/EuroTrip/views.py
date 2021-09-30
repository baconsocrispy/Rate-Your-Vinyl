from django.shortcuts import render, get_object_or_404, redirect
from .eurotripforms import LocationForm
# pulls in the data from all EuroTrip classes
from .models import Location


def eurotriphome (request):
    return render(request, 'eurotriphome.html')


def eurotrip_loccreate(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eurotrip_loccreate')
    else:
        print(form.errors)
        form = LocationForm()
        context = {
            'form': form,
        }
    return render(request, 'eurotrip_loccreate.html', context)





