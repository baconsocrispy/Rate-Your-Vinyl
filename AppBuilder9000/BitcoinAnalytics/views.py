from django.shortcuts import render, redirect
from .forms import CompetitorForm
from .models import Competitor


def home(request):
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_home.html')


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
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_board.html', {'competitionRow': competition})
