from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactForm
from .forms import ConForm


def navbar(request):
    return render(request, "Portfolio/navbar.html")


def PortfolioIndex(request):
    context = addInquiry(request)
    return render(request, "Portfolio_home.html", context)


def navbar(request):
    return render(request, "Portfolio/navbar.html")


def addInquiry(request):
    form = ConForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return context
        else:
            print(form.errors)
    return context

def inqurieslist(request):
    inquries = ContactForm.ContactForm.all()
    context = addInquiry(request)
    context.update({
        'inquries': inquries,
    })

    return render(request, "Portfolio_data.html", context)

def inquiry(request, pk):
    pk = int(pk)
    inquries = get_object_or_404(ContactForm, pk=pk)
    content = {
        'inquries': inquries,
    }
    return render(request, 'portfolio_display.html', content)

def inquriesdetails(request, pk):
    pk = int(pk)
    inquiry = get_object_or_404(ContactForm, pk=pk)
    form = ConForm(data=request.POST or None, instance=inquiry)
    if request.method == 'POST':
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.save()
            return redirect('Portfolio_data')
    else:
        content = {
            'form': form,
            'inquiry': inquiry
        }
        return render(request, 'portfolio_details.html', content)

def inquirydelete(request, pk):
    inquiry = get_object_or_404(ContactForm, pk=pk)
    if request.method == 'POST':
        inquiry.delete()
        # removing primary key value from url
        return redirect('../../Portfolio_data.html')
    content = {'inquiry': inquiry}
    return render(request, 'portfolio_delete.html', content)
