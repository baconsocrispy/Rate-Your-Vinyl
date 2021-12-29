
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Register, Diary
from .forms import UserForm, DiaryForm, LoginForm

# imports needed for Beautiful Soup
import requests
from bs4 import BeautifulSoup


# Create your views here.

def study_home(request):
    registry = Register.objects.all()
    return render(request, 'StudyApp/study_app_home.html', {'registry':registry})

def sign_up(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('members')
        else:
            print(form.errors)
    else:
        context = {
            'form': form,
        }
        return render(request, 'StudyApp/study_app_signup.html', {'form':form})


# Displays diary form when clicked from navbar
"""
    Need to find a way to only allow access to this page once logged in.
    Must figure out a way to first have a properly functioning login page.
    From there, ensure the form submits to the appropriate model 'Diary' not 'Register'
"""
def diary(request):
    form = DiaryForm(request.POST or None)
    if request.method == "OST":
        if form.is_valid():
            form.save()
            return redirect("study_home")
        else:
            print(form.errors)
    else:
        return render(request, "StudyApp/study_app_diary.html", {'form':form})
""" Attempted this code (request, pk):
    pk = pk
    inst = get_object_or_404(Register, pk=pk)
    form = DiaryForm(request.POST or None, instance=inst)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('study_home')
        else:
            print(form.errors)
    else:
        context = {
            'form': form,
        }
        return render(request, 'StudyApp/study_app_diary.html', {'form':form})
    Had errors... """

# displays a login page without functioning buttons
# Must figure out logic to allow authentication of credentials
#   that are already stored in the database
def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    return render(request, 'StudyApp/study_app_login.html', context)

# Renders the member page
# See 'study_app_members.html for logic that displays all items in db
def members(request):
    register = Register.objects.all()
    return render(request, 'StudyApp/study_app_members.html', {'register':register})

def edit(request, pk):
    pk = int(pk)
    inst = get_object_or_404(Register, pk=pk)
    # FMI (For My Information), don't forget to add "data=" to the request.POST
    form = UserForm(data=request.POST or None, instance=inst)
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
#           NOTE TO SELF: FMI, redirect does not need "request, path" just the pattern name will suffice
            return redirect("members")
        else:
            print(form.errors)
    else:
        return render(request, "StudyApp/study_app_edit.html", {'form':form})

def info(request, pk):
    pk = int(pk)
    # the .filter() allows me to get the selected username's info
    register = Register.objects.all().filter(id=pk)
    return render(request, 'StudyApp/study_app_info.html', {'register':register})

# Creating Delete and Confirmation methods for study_app_edit.html
def delete(request, pk):
    pk = int(pk)
    # only the instance selected from the db is needed to delete it
    # you don't have to add the form
    inst = get_object_or_404(Register, pk=pk)
    # if the user presses the delete button, delete item and redirect
    if request.method == "POST":
        inst.delete()
        return redirect("members")
    # note the indentation
    return render(request, "StudyApp/study_app_confirm.html", {'inst':inst})

def confirm(request):
    # yf yes is pressed, delete form with data
    # if no (or else:, return to members page
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('member')
        else:
            return redirect('members')

"""
======================================================
    BEAUTIFUL SOUP SECTION
========================================================================
"""
# NOTE: for this section, you will need to import a method and a class
#   import requests,
#   from bs4 import BeautifulSoup

# Creating the view method that will render the study_app_focu.html template
def focus(request):
    page = requests.get("https://www.sciencenewsforstudents.org/article/top-10-tips-study-smarter-not-longer-study-skills")
    soup = BeautifulSoup(page.content, 'html.parser')
    # Target the html tag I want (which are the h4 tags)
    tips = soup.find_all('h4')
    # creates a tuple containing all ten tips I want to display
    top_ten = (tips[0].get_text(), tips[1].get_text(), tips[2].get_text(), tips[3].get_text(), tips[4].get_text(),
               tips[6].get_text(), tips[7].get_text(), tips[8].get_text(), tips[9].get_text(), tips[10].get_text())
    # use for logic to display each tip as a list
    for item in top_ten:
        print(item)

    return render(request, "StudyApp/study_app_focus.html")

































