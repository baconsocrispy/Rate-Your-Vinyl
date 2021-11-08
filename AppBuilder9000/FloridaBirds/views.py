from django.shortcuts import render, redirect

from .forms import BirdDescriptionForm


# Create your views here.

# View to display home page.

def florida_birds_home(request):
    # render method takes the request object and template name as arguments
    # returns httpResponse object with rendered text.
    return render(request, 'FloridaBirds/FloridaBirds_home.html')

# View to add a bird to database.


def add_bird(request):
    # declare variable called "form".
    form = BirdDescriptionForm(data=request.POST or None)
    if form.is_valid():  # method is used to validate all fields in the user form.
        form.save()
        return redirect('florida_birds_add_bird')  # go back to "add bird url"
    else:
        print(form.errors)
        form = BirdDescriptionForm()
        context = {'form': form}  # dictionary item
    return render(request, 'FloridaBirds/FloridaBirds_add_bird.html', context)
