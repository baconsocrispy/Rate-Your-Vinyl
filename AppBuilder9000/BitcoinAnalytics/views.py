from django.shortcuts import render


def home(request):
    return render(request, 'BitcoinAnalytics/bitcoin_analytics_home.html')