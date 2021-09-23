from django.shortcuts import render

# Create your views here.
def statCheckHome(request):
    return render(request,'StatCheck/StatCheckHOME.html')
