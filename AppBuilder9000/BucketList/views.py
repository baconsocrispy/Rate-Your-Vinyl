from django.shortcuts import render
from .models import bucketItem
from . import views


# renders homepage
def BucketList_home(request):
    return render(request, "BucketList_home.html")

# create page
def BucketList_create(request):
    return render(request, "BucketList_create.html")

