from django.shortcuts import render

posts = [
    {
        'author': 'Karen Kline',
        'title': 'Crypto Today',
        'content': 'First post content',
        'date_posted': 'September 3, 2020'
    },
    {
        'author': 'Susan Brown',
        'title': 'Crypto Is It The Future?',
        'content': 'Second post content',
        'date_posted': 'September 3, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'CryptoAnalytics/crypto_analytics_home.html', context)


def about(request):
    return render(request, 'CryptoAnalytics/about.html', {'title': 'About'})
