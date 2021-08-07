from django.shortcuts import render, redirect, get_object_or_404
from .models import NewPasswords
from .forms import NewPasswordsForm


# Create your views here:
def home(request): # renders the 'home page' @ templates/PwdMgr_home.html
    return render(request, 'PasswordManager/PwdMgr_home.html')


def generator(request):
    form = NewPasswordsForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST': # if the method is POST...
        if form.is_valid(): # ... and all fields are valid...
            form.save() # ...save the form's contents to the database
            return redirect('PwdMgr_home') # return User to this app's Home page
    content = {'form': form}
    return render(request, 'PasswordManager/PwdMgr_generator.html', content) # return form's data within the 'Password Generator' page


def database(request):
    passwords_table = get_object_or_404(NewPasswords)
    content = {'passwords_table': passwords_table}
    return render(request, 'PasswordManager/PwdMgr_database.html', content)
