from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from django.views import generic

class CardListView(generic.ListView):
    model = Card

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

def display(request):
    all_cards = Card.objects.all()
    return render(request, 'sportscards/sportscards_display.html', {'all_cards':all_cards})



def details(request, pk):
    pk = int(pk)
    card = get_object_or_404(Card, pk=pk)
    form = CardForm(data=request.POST or None, instance=card)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            messages.info(request, 'Changes made successfully.')
            return redirect('sportscards_display')
        else:
            print(form.errors)
    else:
        return render(request, 'sportscards/sportscards_details.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('sportscards_display')
    context = {'card': card}
    return render(request, 'sportscards/sportscards_delete.html', context)

