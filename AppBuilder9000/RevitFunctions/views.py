#story1, step4: Add function to views to render the home page
# add function with name matching urls.py views.xxxx (match xxxx), url will call this function and display something on the screen.

from django.shortcuts import render, redirect, get_object_or_404
from .models import RvtFunction, User                                       # MUST import classes
from .forms import AddRvtFunctionForm, AddUserForm                          # MUST import forms

# Create your views here.
def RevitFunctions_home(request):
    return render(request, 'RevitFunctions/RevitFunctions_home.html')

# Story2, step 4: Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
# function for the form: AddRvtFunction
def RevitFunctions_AddRvtFunction(request):
    form = AddRvtFunctionForm(data=request.POST or None)                    # request.POST is referring to the data that comes through when you "post" it from a form.
                                                                                # None is if no data is currently coming through.
                                                                                # does not evaluate to True or False, but returns one of the objects.
                                                                            # When the QueryDict request.POST is empty, it takes a Falsy value, so the item on RHS
                                                                                # of the or operation is selected (which is None), and the form is initialized without
                                                                                # vanilla arguments (i.e. with None): form = MyModelForm()
                                                                                # Otherwise, when request.POST is not empty, the form is initialized with the QueryDict:
                                                                                # form = MyModelForm(request.POST)


    if request.method == 'POST' and form.is_valid():
                                                                            # Django’s login form is returned using the POST method in which the browser
                                                                                # bundles up the form data, encodes it for transmission, sends it to the server,
                                                                                # and then receives back its response.
                                                                            # form.is_valid() = used to perform validation for each field of the form, it is defined
                                                                                # in Django Form class. It returns True if data is valid and place all data into a
                                                                                # cleaned_data attribute.
        form.save()
        return redirect('RevitFunctions_home')                              # go back to home if true.
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddRvtFunction.html', {'form': form})
                                                                            # enter form if false.


# Story2, step 4: Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
# function for the form: AddUser
def RevitFunctions_AddUser(request):
    form = AddUserForm(data=request.POST or None)
    if request.method == 'POST' and form.is_Valid():
        form.save()
        return redirect('RevitFunctions_home')
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddUser.html', {'form': form})


# Story2, Step5: Check the database to make sure your item saves without errors (must check SQLite3 after it generates dB)
# function to see all records of RvtFunctions dB
def RevitFunctions_RvtRecords(request):
    rvtrecords = RvtFunction.RvtFunctions.all()                             # check models.py for proper class and object name.
    return render(request, 'RevitFunctions/RevitFunctions_RvtRecords.html', {'rvtrecords': rvtrecords})



# Story2, Step5: Check the database to make sure your item saves without errors (must check SQLite3 after it generates dB)
# function to see all records of RvtFunctions dB
def RevitFunctions_UserRecords(request):
    userrecords = User.Users.all()                                          # check models.py for proper class and object name.
    return render(request, 'RevitFunctions/RevitFunctions_UserRecords.html', {'userrecords': userrecords})


# Retrive all RevitFunctions
#def RevitFunctions_Details(request, pk):                                   #(request, id): pass id attribute from urls
#    details = RvtFunctionForm(data=request.POST or None)
#    if request.method == 'POST' and form.is_Valid():
#       form.save()
#        return redirect('RevitFunctions_home')
#    else:
#        return render(request, 'RevitFunctions_AddRvtFunction.html', {'form': form})
def RevitFunctions_futureNav3(request):
    return render(request, 'RevitFunctions/RevitFunctions_futureNav3.html')
