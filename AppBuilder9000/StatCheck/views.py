from django.shortcuts import render

# Create your views here.
def StatCheckHome(request):
    return render(request,'StatCheck/StatCheckHOME.html')
