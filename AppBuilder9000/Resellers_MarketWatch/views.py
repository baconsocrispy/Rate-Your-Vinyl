from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WebscrapeForm, UserLoginForm
from .models import WebScrape, UserLogin
# Create your views here.


def home(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MarketWatch_home.html')
    else:
        form = UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'Resellers_MarketWatch/MarketWatch_home.html', context)


def account(request):
    form = WebscrapeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Resellers_MarketWatch/AccountPage.html')
    else:
        form = WebscrapeForm()
        context = {
            'form': form
        }
        return render(request, 'Resellers_MarketWatch/AccountPage.html', context)

#  UserLogin
def register(request):
    return render(request, 'Resellers_MarketWatch/Register.html')

def Retrieve_ListView(request):
    dataset = UserLogin.User.all()
    return render(request, 'listview.html', {'dataset': dataset})

def Retrieve_DetailView(request,_id):
    try:
        data = UserLogin.User.get(id=_id)
    except UserLogin.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request, 'detailview.html', {'data': data})




