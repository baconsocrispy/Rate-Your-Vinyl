from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
    """Function to open the homepage."""
    return render(request, 'ItemsApp/home.html')


def new_item(request):
    """Creates the form used for user input"""
    form = ItemForm(data=request.POST or None)  # Creates the form from forms.py.
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('itemsApp_home')  # When the form is created, redirect to the home page.
    content = {'form': form}  # Dictionary for form data entry.
    return render(request, 'ItemsApp/new_item.html', content)


def display_items(request):
    """Creates a form displaying the current items in the database."""
    item = Item.objects.all().values()  # Grabs all values from all items in the database.
    content = {'item': item}  # Dictionary for the items.
    return render(request, 'ItemsApp/display_items.html', content)
