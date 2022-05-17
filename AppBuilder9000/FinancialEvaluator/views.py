from django.shortcuts import render
from .models import Account


def fe_Home(request):
    return render(request, 'FinancialEvaluator/fe_Home.html')


