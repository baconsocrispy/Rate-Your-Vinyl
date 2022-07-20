from django.shortcuts import render


# renders homepage
def home(request):
    return render(request, "BucketList_home.html", {})
