from django.shortcuts import render, get_object_or_404, redirect
from .models import Register
from .forms import UserForm

# Create your views here.

def study_home(request):
    registry = Register.objects.all()
    return render(request, 'StudyApp/study_app_home.html', {'registry':registry})

def sign_up(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('study_home')
    else:
        print(form.errors)
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'StudyApp/study_app_signup.html', {'form':form})


