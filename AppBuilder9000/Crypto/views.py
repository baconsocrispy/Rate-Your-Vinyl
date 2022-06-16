from django.shortcuts import render, redirect
from .forms import AddCryptoForm
from .models import AddCrypto
# Create your views here.
def crypto_home(request):
    return render(request, 'Crypto/Crypto_Home.html')

# function to render built in form from my model AddCrypto
def crypto_addcrypto(request):
    form = AddCryptoForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'Crypto/Crypto_AddCrypto.html', content)

# function to fetch all objects created from form and render
def crypto_ratings(request):
    crypto_entries = AddCrypto.objects.all()
    content = {'crypto_entries': crypto_entries}
    return render(request, 'Crypto/Crypto_Ratings.html', content)