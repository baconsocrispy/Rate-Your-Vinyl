from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'CryptoAnalytics/crypto_analytics_home.html', context)


def about(request):
    return render(request, 'CryptoAnalytics/about.html', {'title': 'About'})
