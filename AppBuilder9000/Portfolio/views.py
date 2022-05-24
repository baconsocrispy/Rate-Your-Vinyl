from django.shortcuts import render, redirect
from .models import ContactForm
from .forms import ConForm

def PortfolioIndex(request):
    return render(request, "Portfolio_home.html")


def navbar(request):
    return render(request, "Portfolio/navbar.html")


def addInquiry(request):
    form = ConForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Portfolio_data.html')
        else:
            print(form.errors)
            form = ConForm()
        context = {
            'form': form,
        }
    return render(request, "Portfolio_base.html", context)


def inqurieslist(request):
    inquries = ContactForm.ContactForm.all()
    context = {
        'inquries': inquries,
    }
    return render(request, "Portfolio_data.html", context)

