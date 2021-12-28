
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



def diary(request):
    form = DiaryForm(request.POST or None)
    if request.method == "OST":
        if form.is_valid():
            form.save()
            return redirect(request, "StudyApp/study_app_home.html")
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

def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    return render(request, 'StudyApp/study_app_login.html', context)

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
            return redirect('members')
        else:
            print(form.errors)
    else:
        return render(request, "StudyApp/study_app_edit.html", {'form':form})

def info(request, pk):
    pk = int(pk)
    # the .filter() allows me to get the selected username's info
    register = Register.objects.all().filter(id=pk)
    return render(request, 'StudyApp/study_app_info.html', {'register':register})





































