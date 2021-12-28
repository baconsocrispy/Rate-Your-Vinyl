
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Register, Diary
from .forms import UserForm, DiaryForm, LoginForm


# Create your views here.

def study_home(request):
    registry = Register.objects.all()
    return render(request, 'StudyApp/study_app_home.html', {'registry':registry})

def sign_up(request):
    form = UserForm(request.POST or None)
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

# Shows all items of a particular member selected from 'Register' model
# NOTE: Update button is not functional.. fix upon submission of story 4
def info(request, pk):
    pk = int(pk)
    inst = get_object_or_404(Register, pk=pk)
    form = UserForm(data=request.POST or None, instance=inst)
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
#           NOTE TO SELF: FMI, redirect does not need "request, path" just the pattern name will suffice
#               You'll get an error if you add "request" so be sure not to
            return redirect("members")
        else:
            print(form.errors)
    else:
        return render(request, "StudyApp/study_app_info.html", {'form':form})




































