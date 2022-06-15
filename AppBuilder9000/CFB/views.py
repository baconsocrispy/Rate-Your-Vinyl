from django.shortcuts import render

# Create your views here.
def CFB_Home(request):
    return render(request, 'CFB/CFB_Home.html')
