from django.shortcuts import render, redirect
from .forms import sneakerForm

def Sneakers_home(request):
    return render(request, "Sneakers/Sneakers_home.html")


def create_sneaker(request):
	form = sneakerForm(data=request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('../')
	content = {'form': form}
	return render(request, "Sneakers/Sneakers_createSnkr.html", content)
	""" Pull all fields from account and puts inside variable form. Then checks if
		request method is post and if it is it well redirect user to index page. 
		Then sends them to create a new account"""