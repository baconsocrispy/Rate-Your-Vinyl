from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.views.generic import FormView
from .models import Yoga
from .forms import YogaForm


# Adding function to render home page.
def home(request):
    return render(request, 'Practicing_Yoga/yoga_home.html')

def create(request):
    form = YogaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('yoga_create')
    else:
        print(form.errors)
        form = YogaForm()
    context = {
        'form': form,
    }
    return render(request, 'Practicing_Yoga/yoga_create.html', context)
