from django.shortcuts import render
from .models import FunkoPopName
from .forms import CollectionForm
from django.http import HttpResponseRedirect
from django.db.models import Q


def funkocollectorhome(request):
    return render(request, 'funkocollectorhome.html')

# function for rendering a form for adding to the CollectionForm database from the web page addcollection.html


def addcollection(request):
    submitted = False
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('addcollection?submitted=True')
    else:
        form = CollectionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addcollection.html', {'form': form, 'submitted': submitted})

# function for rendering a information saved from the CollectionForm database to the web page collection.html


def collection(request):
    collectionpop = FunkoPopName.objects.all()
    return render(request, 'collection.html', {'collectionpop': collectionpop})

# function for rendering an information page from a search box in the nav bar.  Will render all information from a
# database from a search criteria inputted into the search box.


def searchcollection(request):
    if request.method == "POST":

        searched = request.POST['searched']
        pops = FunkoPopName.objects.filter(Q(name__contains=searched) | Q(size__contains=searched) |
                                           Q(fandome__contains=searched) | Q(chase__contains=searched) |
                                           Q(purchase_price__contains=searched) | Q(value__contains=searched))

        return render(request, 'searchcollection.html', {'searched': searched, 'pops': pops})
    else:
        return render(request, 'searchcollection.html', {})
