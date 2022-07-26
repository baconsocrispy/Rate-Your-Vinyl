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

# renders list page
def BucketList_list(request):
    queryset = bucketItem.objects.all()  # list of bucketlist items
    context = {
        "item_list": queryset
    }
    return render(request, "BucketList/BucketList_list.html", context)

# details of each item in database
def BucketList_details(request, pk):
    item = get_object_or_404(bucketItem, pk=pk)
    content = {'item': item}
    return render(request, "BucketList/BucketList_details.html", content)

# Update function
def BucketList_update(request, pk):
    item = get_object_or_404(bucketItem, pk=pk)
    form = BucketItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../list')
    content = {'form': form, 'item': item}
    return render(request, 'BucketList/BucketList_update.html', content)

# Delete/remove function
def BucketList_delete(request, pk):
    item = get_object_or_404(bucketItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('../../list')
    content = {'item': item}
    return render(request, 'BucketList/BucketList_delete.html', content)

