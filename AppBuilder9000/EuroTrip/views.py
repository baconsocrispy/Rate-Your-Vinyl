from django.shortcuts import render, get_object_or_404, redirect
from .forms import LocationForm
# pulls in the data from all EuroTrip classes
from .models import Location


def eurotriphome(request):
    return render(request, 'eurotriphome.html')


def eastern(request):
    return render(request, 'eastern.html')


def easternlocationscreate(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('easternlocationscreate')
    else:
        print(form.errors)
        form = LocationForm()
        context = {
            'form': form,
        }
    return render(request, 'easternlocationscreate.html', context)


def eastern_list(request):
    location_list = Location.objects.all()
    return render(request, 'templates/eastern.html',
            {'location_list': location_list})






