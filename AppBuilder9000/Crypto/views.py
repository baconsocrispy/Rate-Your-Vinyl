from django.shortcuts import render, redirect
from .forms import AddCryptoForm

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
