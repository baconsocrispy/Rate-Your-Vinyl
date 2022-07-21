from django.shortcuts import render, redirect
from .models import bucketItem
from . import views
from .forms import BucketItemForm


# renders homepage
def BucketList_home(request):
    return render(request, "BucketList/BucketList_home.html")


# create page
def BucketList_create(request):
    form = BucketItemForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BucketList_home')
    content = {'form': form}
    return render(request, "BucketList/BucketList_create.html", content)
