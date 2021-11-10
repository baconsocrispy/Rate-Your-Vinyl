from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment

from .models import BirdDescription
from .forms import BirdDescriptionForm
from django.http import HttpResponseRedirect


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


# View to display all birds from database.

def display_all_birds(request):
    bird_data = BirdDescription.objects.all()
    return render(request, "FloridaBirds/FloridaBirds_display_all_birds.html", {'bird_data': bird_data})


# View to display detail of one bird from the display_all_birds file.

def display_details(request, pk):
    birddetail = BirdDescription.objects.get(pk=pk)
    return render(request, "FloridaBirds/FloridaBirds_details.html", {"birddetail": birddetail})

# View to search for a particular bird using the search box


# def search_collection(request):
# if request.method == "POST":
# searched = request.POST['searched']
# birds = BirdDescription.objects.filter(Q(name__contains=searched))

# return render(request, 'FloridaBirds/FloridaBirds_search_collection.html',
# {'searched': searched, 'birds': birds})
# else:
# return render(request, 'FloridaBirds/FloridaBirds_search_collection.html', {})
