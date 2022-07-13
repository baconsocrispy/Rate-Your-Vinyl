from django.shortcuts import render


# Create your views here.


def ET_Home(request):
	return render(request, 'Expense_Tracker/ET_Home.html')


def ET_Account(request):
	return render(request, 'Expense_Tracker/ET_Account.html')


def admin(request):
	return render(request, 'Expense_Tracker/admin.html')
