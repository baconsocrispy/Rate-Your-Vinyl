from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivitiesForm
from .models import Activities


def oregon_home(request):
    return render(request, 'Oregon_City/Oregon_home.html')


def oregon_create(request):
    form = ActivitiesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('oregon_display')
    content = {'form': form}
    return render(request, 'Oregon_City/Oregon_create.html', content)


def oregon_display(request):
    oregon_details = Activities.activity_name
    content = {'details': oregon_details}
    return render(request, 'Oregon_City/Oregon_display.html', content)


def oregon_details(request, pk):
    details = get_object_or_404(Activities, pk=pk)
    content = {'details': details}
    return render(request, 'Oregon_City/Oregon_details.html', content)


def oregon_view(request):
    activity = Activities.ActivitiesManager.all()
    content = {'Activity': activity}
    return render(request, 'Oregon_City/Oregon_view.html', content)
