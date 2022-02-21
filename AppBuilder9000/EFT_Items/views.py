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


def eft_all_items(request):
    # Gets all objects from the database sorted by name
    sorted_items = EFTItems.objects.order_by('name')
    return render(request, 'EFT_Items/EFT_Items_display_items.html', {'items': sorted_items})


def eft_details(request, pk):
    details = get_object_or_404(EFTItems, pk=pk)
    context = {
        'details': details,
    }
    return render(request, 'EFT_Items/EFT_Items_details.html', context)
