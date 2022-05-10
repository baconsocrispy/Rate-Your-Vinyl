from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from itertools import chain
from .forms import coachForm, childForm
from .models import Coach, Child


# Create your views here.
def coachHome(request):
    form = coachForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return coachCreate(request, pk)
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

#def childRoster(request, pk):
    #coach = account.accounts.filter(coach_Grade=pk)
    #child = singupChild.signupChilds.filter(Grade=pk)
    #table_contents = { }
    #content = {'coach': coach, 'table_contents': table_contents, 'child': child}
    #return render(request, 'Jobs/coachChildSignups.html', content)

#def childRoster(request):
    #cursor=connection.cursor()
    #cursor.execute("select singupChild.grade,singupChild.child_Name,account.name from singupChild join account on singupChild.grade=account.coach_Grade")
    #results=cursor.fetchall()
    #return render(request,'childRoster.html',{'singupChild':results})

def childDetails(request, pk):
        details = get_object_or_404(Child, pk=pk)
        content = {'details': details}
        return render(request, 'Jobs/coachChildDetails.html', content)