from django.shortcuts import render, get_object_or_404, HttpResponse

def zoo_home(request):
    return render(request, 'zoo_home.html')
