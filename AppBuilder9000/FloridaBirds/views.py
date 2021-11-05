from django.shortcuts import render, redirect

from .forms import BirdDescriptionForm


# Create your views here.

# View to display home page.

def florida_birds_home(request):
    return render(request, 'FloridaBirds/FloridaBirds_home.html')

# View to add a bird to database.


def add_bird(request):
    form = BirdDescriptionForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('florida_birds_add_bird')
    else:
        print(form.errors)
        form = BirdDescriptionForm()
        context = {'form': form}
    return render(request, 'FloridaBirds/FloridaBirds_add_bird.html', context)
