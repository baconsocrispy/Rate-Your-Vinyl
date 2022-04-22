from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


def StockMarketHome(request):
    return render(request, 'StockMarketHome.html')


def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("StockMarketHome")
    content = {'form': form}
    return render(request, 'StockMarketCreate.html', content)


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'StockMarketTransaction.html', content)



def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'StockMarketTransaction.html', content)


def display(request):
    all_entries = Account.Accounts.all()
    content = {'all_entries': all_entries}
    return render(request, 'StockMarketDisplay.html', content)


def details(request, pk):
    selected = get_object_or_404(Account, pk=pk)
    content = {'selected': selected}
    return render(request, "StockMarketDetails.html", content)
