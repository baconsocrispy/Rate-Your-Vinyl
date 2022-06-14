from django.shortcuts import render


# Create your views here.
def crypto_home(request):
    return render(request, 'Crypto/Crypto_Home.html')
