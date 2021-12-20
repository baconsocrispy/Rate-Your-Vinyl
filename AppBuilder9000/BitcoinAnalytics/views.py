from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompetitorForm
from .models import Competitor


def home(request):
    form = CompetitorForm(data=request.POST or None)
    competitors = Competitor.Competition.all()
    if request.method == 'POST' and 'name' in request.POST.keys():
        print(request.POST)
        pk = request.POST['name']
        print("PK", pk)
        return selection(request, pk)
    content = {'form': form, 'competitors': competitors}
    print(content)
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_home.html', content)


def selection(request, pk):
    competitor = Competitor.Competition.filter(name=pk)
    content = {'competitionRow': competitor}
    print(content)
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_competitor_details.html', content)


def create_competitor(request):
    form = CompetitorForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('bitcoin_analytics_home')
    content = {'form': form}
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_add_competitor.html', content)


def show_competition(request):
    competition = Competitor.Competition.all()
    if request.method == 'POST':
        print(request.POST)
        pk = request.POST['name']
        return selection(request, pk)

    return render(request, 'BitcoinAnalytics/bitcoin_analytics_board.html', {'competitionRow': competition})


# def show_details(request):
#     form = CompetitorListForm(data=request.POST or None)
#     content = {'form': form}
#     return render(request, 'BitcoinAnalytics/bitcoin_analytics_competitor_details.html', content)
