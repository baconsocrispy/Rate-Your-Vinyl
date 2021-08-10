from django.shortcuts import render, redirect, get_object_or_404
from .models import NewPassword
from .forms import NewPasswordForm
from django.core.paginator import Paginator


# Create your views here:
def home(request): # renders the 'home page' @ templates/PwdMgr_home.html
    return render(request, 'PasswordManager/PwdMgr_home.html')


def database(request):
    allPasswords = NewPassword.NewPasswords.filter(id__gt=0) # returns a filtered dictionary of key:value pairs from all 9 db fields ('id' through 'Favorite')
    # content = {'allPasswords': allPasswords} # the QuerySet (from above) becomes the k:v pair needed within 'content' (thanks Forest!)
    paginator = Paginator(allPasswords, 10) # displays 10 passwords per page; overflow == a new, 'next' page

    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return render(request, 'PasswordManager/PwdMgr_database.html', {'content': content})


def details(request):
    allPasswords = NewPassword.NewPasswords.all()
    content = {'allPasswords': allPasswords}
    paginator = Paginator(allPasswords, 5)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return render(request, 'PasswordManager/PwdMgr_details.html', {'content': content})



def generator(request):
    form = NewPasswordForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST': # if the method is POST...
        if form.is_valid(): # ... and all fields are valid...
            form.save() # ...save the form's contents to the database
            return redirect('PwdMgr_home') # return User to this app's Home page
    content = {'form': form}
    return render(request, 'PasswordManager/PwdMgr_generator.html', content) # return form's data within the 'Password Generator' page



