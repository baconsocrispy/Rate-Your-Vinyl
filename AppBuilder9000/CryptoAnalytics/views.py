from django.contrib import messages

from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def home(request):
    return render(request, 'CryptoAnalytics/crypto_analytics_home.html')


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

