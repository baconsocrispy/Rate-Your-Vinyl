from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from itertools import chain
from .forms import coachForm, childForm
from .models import Coach, Child


# Create your views here.
def coachHome(request):
    form = coachForm(data=request.POST or None)
    if request.method == 'POST':
        return coachCreate(request)
    content = {'form': form}
    return render(request, 'Jobs/coachHome.html', content)

def coachCreate(request):
    form = coachForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Jobs/coachCreate.html', content)

def childCreate(request):
    form = childForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Jobs/coachChildCreate.html', content)

def childRoster(request):
    rosterList = Child.Children.all().order_by('Child_Grade')
    content = {'rosterList': rosterList}
    return render(request, 'Jobs/coachChildRoster.html', content)


def childDetails(request, pk):
    details = get_object_or_404(Child, pk=pk)
    content = {'details': details}
    return render(request, 'Jobs/coachChildDetails.html', content)

def childUpdate(request, pk):
    details = Child.Children.get(pk=pk)
    form = childForm(request.POST or None, instance=details)

    if form.is_valid():
        form.save()
        return redirect('coachChildRoster')

    content = {'details': details, 'form': form}
    return render(request, 'Jobs/coachUpdateChild.html',content)

def childDelete(request, pk):
    childForDelete = get_object_or_404(Child, pk=pk)

    if request.method == "POST":
        childForDelete.delete()
        return redirect('coachChildRoster')
    content = {'childForDelete': childForDelete}
    return render(request, 'Jobs/coachChildDelete.html', content)

#This code adds some kids to the roster of the roster is empty. Helpful for demo function!
cFName = ['Aman', 'Vijay', 'Casey', 'Katelyn', 'Jessica', 'Chris', 'Lacy', 'Luis']
cLName = ['Jones', 'Vitali', 'Adams', 'Flaherty', 'Jones', 'Cringle', 'Lewis', 'Lopez']
cGrade = ['K-1st', 'K-1st', '2nd-3rd', '2nd-3rd', '4th-5th', '4th-5th', '6th-7th', '6th-7th']
cJersey = [10,23,45,34,56,67,10,15]
pName = ['Bob Jones', 'Pchenka Vitali', 'Phil Adams', 'Laura Flaherty', 'Jason Jones', 'Mrs. Cringle', 'Samantha Lewis']
pPhone = [5033458567,5033678567,5033456798,5032345467,5031459689,5452456567,5034576833,5031234567]
pEmail = ['Bob@gmail.com', 'Pchenka@gmail.com', 'Phil@gmail.com', 'Laura@gmail.com', 'Jason@gmail.com', 'naughtyornice@gmail.com', 'Lulu@gmail.com']
notesOrAllergies = ['Bob@gmail.com', 'Pchenka@gmail.com', 'Phil@gmail.com', 'Laura@gmail.com', 'Jason@gmail.com', 'naughtyornice@gmail.com', 'Lulu@gmail.com']


def addChildren(request, *args, **kwargs):
    # Iterate through all the data items
    for i in range(len(cFName)):
        # Insert in the database
        Child.children.create(First_Name=cFName[i], Last_Name=cLName[i], Child_Grade=cGrade[i])

    # Getting all the stuff from database
    query_results = Student.objects.all();

    # Creating a dictionary to pass as an argument
    content = {'query_results': query_results}

    # Returning the rendered html
    return render(request, "home.html", content)
