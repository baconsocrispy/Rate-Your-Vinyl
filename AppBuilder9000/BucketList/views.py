from django.shortcuts import render, redirect, get_object_or_404
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


def BucketList_list(request):
    queryset = bucketItem.objects.all()  # list of bucketlist items
    context = {
        "item_list": queryset
    }
    return render(request, "BucketList/BucketList_list.html", context)


def BucketList_details(request, pk):
    item = get_object_or_404(bucketItem, pk=pk)
    content = {'item': item}
    return render(request, "BucketList/BucketList_details.html", content)
