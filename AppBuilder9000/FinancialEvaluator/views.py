from django.shortcuts import render, redirect
from .forms import EvaluationForm
from .models import Evaluation, Approach, Account



def fe_Home(request):
    return render(request, 'FinancialEvaluator/fe_Home.html')


def fe_Read(request):
    entry = Evaluation.Evaluations.all()
    content = {'entry': entry}
    return render(request, 'FinancialEvaluator/fe_Read.html', content)

def fe_Evaluation(request):
    form = EvaluationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fe_Read')
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'FinancialEvaluator/fe_Evaluation.html', content)


def fe_Account(request):
    return render(request, 'FinancialEvaluator/fe_Account.html')

def fe_Approach(request):
    return render(request, 'FinancialEvaluator/fe_Approach.html')


def admin(request):
    return render(request, 'FinancialEvaluator/admin.html')

def fe_Delete(request):
    return render(request, 'FinancialEvaluator/fe_Delete.html')

def fe_Update(request):
    return render(request, 'FinancialEvaluator/fe_Update.html')

def fe_Details(request):
    return render(request, 'FinancialEvaluator/fe_Details.html')
