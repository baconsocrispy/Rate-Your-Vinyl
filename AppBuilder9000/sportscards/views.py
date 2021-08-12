from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm


def home(request):
    types = ["Baseball", "Basketball", "Hockey", "Football"]
    context = {
        'types': types,
    }
    return render(request, "sportscards/sportscards_home.html", context)

def join(request):
    form = CardForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("SportsCards_join")

    return render(request, 'sportscards/join.html', {"form":form})
