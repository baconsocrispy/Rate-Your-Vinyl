from django.shortcuts import render


# Create your views here.

def study_home(request):
    return render(request, 'StudyApp/study_app_home.html')
