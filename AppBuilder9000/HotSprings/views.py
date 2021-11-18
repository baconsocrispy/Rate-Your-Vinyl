from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .form import hotspringsForm
from .models import HotSprings



def hotsprings_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'hotsprings_home.html')


def add_hotsprings(request):
    form = hotspringsForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('hotsprings_list')
    else:
        print(form.errors)
        form = hotspringsForm()
        context = {'form' : form}
    return render(request, 'hotsprings_create.html', context)

def list_hotsprings(request):
    hotsprings = HotSprings.objects.all()
    return render(request, 'hotsprings_list.html', {'hotsprings': hotsprings})



