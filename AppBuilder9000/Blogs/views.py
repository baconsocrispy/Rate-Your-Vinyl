from django.shortcuts import render


def blogs(request):
    return render(request, 'blogs_home.html')


def new_entry(request):
    return render(request, 'new_entry.html')

