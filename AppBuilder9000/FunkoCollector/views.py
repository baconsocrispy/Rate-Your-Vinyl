from django.shortcuts import render, redirect
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

# function for rendering a details page from a clickable link found by the pk-id of an object in the database
# to display the details of that one object.


def detailscollection(request, funkopopname_id):
    detailspop = FunkoPopName.objects.get(pk=funkopopname_id)
    return render(request, 'detailscollection.html', {'detailspop': detailspop})

def update_collection(request, funkopopname_id):
    editpop = FunkoPopName.objects.get(pk=funkopopname_id)
    form = CollectionForm(request.POST or None, instance=editpop)
    if form.is_valid():
        form.save()
        return redirect('collection')
    return render(request, 'editcollection.html', {'editpop': editpop, 'form': form})


def delete_pop(request, funkopopname_id):
    deletepop = FunkoPopName.objects.get(pk=funkopopname_id)
    deletepop.delete()
    return redirect('collection')


