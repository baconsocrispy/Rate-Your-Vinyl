#story1, step4: Add function to views to render the home page
# add function with name matching urls.py views.xxxx (match xxxx), url will call this function and display something on the screen.

from django.shortcuts import render, redirect, get_object_or_404            # get_object_or_404 = This function calls the given model and get object from that if that object or model doesn’t exist it raise 404 error.
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
                                                                            # POST request sends the information from the form to the server, The server processes the information from the Post request
                                                                                # The server responds by displaying whatever success or failure response it has
                                                                            # When the QueryDict request.POST is empty, it takes a Falsy value, so the item on RHS
                                                                                # of the or operation is selected (which is None), and the form is initialized without
                                                                                # vanilla arguments (i.e. with None): form = MyModelForm()
                                                                                # Otherwise, when request.POST is not empty, the form is initialized with the QueryDict:
                                                                                # form = MyModelForm(request.POST)


    if request.method == 'POST':
        if form.is_valid():
                                                                            # Django’s form is returned using the POST method in which the browser
                                                                                # bundles up the form data, encodes it for transmission, sends it to the server,
                                                                                # and then receives back its response.
                                                                            # form.is_valid() = used to perform validation for each field of the form, it is defined
                                                                                # in Django Form class. It returns True if data is valid and place all data into a
                                                                                # cleaned_data attribute.
            form.save()
            return redirect('RevitFunctions_home')                          # go back to home if true.
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddRvtFunction.html', {'form': form})
                                                                            # enter form if false.


# Story2, step 4: Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
# function for the form: AddUser
def RevitFunctions_AddUser(request):
    form = AddUserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RevitFunctions_home')
    else:
        return render(request, 'RevitFunctions/RevitFunctions_AddUser.html', {'form': form})


# Story3, Step2: Add in a function that gets all the items from the database and sends them to the template
# function to see/retrieve all records of RvtFunctions dB
def RevitFunctions_RvtRecords(request):
    rvtrecords = RvtFunction.RvtFunctions.all()                             # check models.py for proper class and object name (class attribute name.variable attributes name)
    return render(request, 'RevitFunctions/RevitFunctions_RvtRecords.html', {'rvtrecords': rvtrecords})


# story4, Step2: Create a views function that will find a single item from the database and send it to the template
# function to see/retrieve details of one item in records by primary key match
def RevitFunctions_RvtDetails(request, pk):
    rvtdetails = get_object_or_404(RvtFunction, pk=pk)                      # check models.py for proper class and object name (class attribute name.variable attributes name)
                                                                            # match the primary key to query that particular item, then assign them into rvtdetails.
    return render(request, 'RevitFunctions/RevitFunctions_RvtDetails.html', {'rvtdetails': rvtdetails})


# Story5, step3: Have the views function send the information for the single item and save any changes.
# function for the form: RvtEdit.html
def RevitFunctions_RvtEdit(request, pk):
    rvtedit = get_object_or_404(RvtFunction, pk=pk)                         # check models.py for proper class and object name (class attribute name.variable attributes name)

    # Use model forms and instances to display the content of a single item from the database
    form = AddRvtFunctionForm(data=request.POST or None, instance=rvtedit)  # instance=rvtedit will populate the cell with the original values.
                                                                            # use the same form as AddRvtFunctionForm
                                                                            # https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django
                                                                            # request.POST is referring to the data that comes through when you "post" it from a form.
                                                                                # None is if no data is currently coming through.
                                                                                # does not evaluate to True or False, but returns one of the objects.
                                                                            # When the QueryDict request.POST is empty, it takes a Falsy value, so the item on RHS
                                                                                # of the or operation is selected (which is None), and the form is initialized without
                                                                                # vanilla arguments (i.e. with None): form = MyModelForm()
                                                                                # Otherwise, when request.POST is not empty, the form is initialized with the QueryDict:
                                                                                # form = MyModelForm(request.POST)


    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        if form.is_valid():
                                                                            # Django’s form is returned using the POST method in which the browser
                                                                                # bundles up the form data, encodes it for transmission, sends it to the server,
                                                                                # and then receives back its response.
                                                                            # form.is_valid() = used to perform validation for each field of the form, it is defined
                                                                                # in Django Form class. It returns True if data is valid and place all data into a
                                                                                # cleaned_data attribute.
            form.save()
            return redirect('RevitFunctions_RvtRecords')                    # go back to home if true.
    else:
        return render(request, 'RevitFunctions/RevitFunctions_RvtEdit.html', {'form': form})
                                                                            # enter form if false.


def RevitFunctions_RvtDelete(request, pk):
    rvtdelete = get_object_or_404(RvtFunction, pk=pk)
    form = AddRvtFunctionForm(request.POST or None, instance=rvtdelete)

    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        rvtdelete.delete()
        return redirect('RevitFunctions_RvtRecords')

    return render(request, 'RevitFunctions/RevitFunctions_RvtConfirmDelete.html', {'rvtdelete': rvtdelete})

def RevitFunctions_RvtConfirmDelete(request):
    if request.method == 'POST':                                            # if this method='POST', the template must have something referrencing this for it to POST somthing.
        form = AddRvtFunctionForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('RevitFunctions_RvtRecords')
    else:
        return render(request, 'RevitFunctions/RevitFunctions_RvtRecords.html')
