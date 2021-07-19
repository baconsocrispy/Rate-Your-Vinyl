from django.shortcuts import render


def home(request):
    return render(request, "Novels/Novels_home.html")
