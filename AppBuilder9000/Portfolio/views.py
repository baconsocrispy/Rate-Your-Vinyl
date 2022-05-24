from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactForm
from .forms import ConForm


def navbar(request):
    return render(request, "Portfolio/navbar.html")


def PortfolioIndex(request):
    context = addInquiry(request)
    return render(request, "Portfolio_home.html", context)


def navbar(request):
    return render(request, "Portfolio/navbar.html")


def addInquiry(request):
    form = ConForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return context
        else:
            print(form.errors)
    return context

