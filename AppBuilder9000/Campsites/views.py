from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .form import CampsitesForm
from .models import CampSites


def campsites_home(request):
    return render(request, 'campsites_home.html')


def add_campsites(request):
    form = CampsitesForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('campsites_list')
    else:
        print(form.errors)
        form = CampsitesForm()
        context = {'form': form}
    return render(request, 'campsites_create.html', context)


def list_campsites(request):
    campsites = CampSites.Sites.all()
    return render(request, 'campsites_list.html', {'campsites': campsites})


def campsites_details(request, pk):
    details = get_object_or_404(CampSites, pk=pk)
    context = {'details': details}
    return render(request, 'campsites_details.html', context)


# update view for details
def update_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(CampSites, id=pk)

    # pass the object as instance in form
    form = CampsitesForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + pk)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)

