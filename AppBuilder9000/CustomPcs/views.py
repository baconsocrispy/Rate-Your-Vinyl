from django.shortcuts import render


# Creating the view

def CustomPcs_home(request):
    return render(request, 'CustomPcs/CustomPcs_home.html')
