from django.shortcuts import render, redirect
from .models import NewPassword
from .forms import NewPasswordForm
from django.core.paginator import Paginator


# Displays the 'HOME PAGE':
def home(request):
    return render(request, 'PasswordManager/PwdMgr_home.html')


# Displays the SELECTED PASSWORD's DETAILS:
def passwordDetails(request):
    allPasswords = NewPassword.NewPasswords.all()
    content = {'allPasswords': allPasswords}
    paginator = Paginator(allPasswords, 5)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return render(request, 'PasswordManager/PwdMgr_details.html', {'content': content})


# Displays the "SAVE A NEW PASSWORD" form:
def passwordInput(request):
    form = NewPasswordForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST': # if the method is POST...
        if form.is_valid(): # ... and all fields are valid...
            form.save() # ...save the form's contents to the database
            return redirect('PwdMgr_home') # return User to this app's Home page
    content = {'form': form}
    return render(request, 'PasswordManager/PwdMgr_pwdInput.html', content) # return form's data within the 'Password Generator' page


# Displays ALL SAVED PASSWORDS (as a list; no details):
def passwordsList(request):
    allPasswords = NewPassword.NewPasswords.filter(id__gt=0) # returns a filtered dictionary of key:value pairs from all 9 db fields ('id' through 'Favorite')
    paginator = Paginator(allPasswords, 10) # displays 10 passwords per page; overflow == a new, 'next' page
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return render(request, 'PasswordManager/PwdMgr_pwdsList.html', {'content': content})