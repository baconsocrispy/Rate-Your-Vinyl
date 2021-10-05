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
    return render(request, 'eastern.html',
            {'location_list': location_list})

# Function to allow user to view a single item


def eurotripdetails(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    form = LocationForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('eastern')
        else:
            print(form.errors)
    else:
        return render(request, 'durotripdetails.html', {'form': form})
