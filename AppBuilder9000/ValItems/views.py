from django.shortcuts import render


def Val_home(request):
    return render(request, 'ValItems/Val_home.html')
