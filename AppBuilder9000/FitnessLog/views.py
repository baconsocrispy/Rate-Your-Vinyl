from django.shortcuts import render


# user story 1
def fitness_home(request):
    return render(request, 'FitnessLog/fitness_home.html')

