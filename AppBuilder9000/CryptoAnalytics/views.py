from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegisterForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'CryptoAnalytics/crypto_analytics_home.html', context)


def about(request):
    return render(request, 'CryptoAnalytics/about.html', {'title': 'About'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('crypto_home')
        else:
            form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})

