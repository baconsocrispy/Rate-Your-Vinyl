from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm


# Create your views here.
def eb_home(request):
    return render(request, 'EmpireBuilder/eb_home.html')

def admin_console(request):
    EmpireBuilder = Booking.objects.all()
    return render(request, 'EmpireBuilder/eb_reservation.html', {'EmpireBuilder': EmpireBuilder})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Booking, pk=pk)
    form = BookingForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('eb_home')
        else:
            print(form.errors)


def cancel(request, pk):
    pk = int(pk)
    item = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        item.cancel()
        return redirect('eb_home')
    context = {'item': item}
    return render(request, 'eb_home', context)

def eb_reserve(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eb_home')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'EmpireBuilder/eb_reservation.html', context)
