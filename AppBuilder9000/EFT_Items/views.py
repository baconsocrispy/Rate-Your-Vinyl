from django.shortcuts import render


# Create your views here.
def eft_home(request):
    return render(request, 'EFT_Items/EFT_Items_home.html')
