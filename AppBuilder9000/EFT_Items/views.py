from django.shortcuts import render, get_object_or_404, redirect
from .models import EFTItems
from .forms import EFTForm


# Create your views here.
def eft_home(request):
    return render(request, 'EFT_Items/EFT_Items_home.html')


def eft_create_record(request):
    form = EFTForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eft_create_record')
    else:
        print(form.errors)
        form = EFTForm()
    context = {
        'form': form,
    }
    return render(request, 'EFT_Items/EFT_Items_create.html', context)
