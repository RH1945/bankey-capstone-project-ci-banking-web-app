from django.shortcuts import render
from .models import Transaction


# Create your views here.


def account_view(request):
    return render(request, "bankey_account/account.html")

def statement(request):
    return render(request, "bankey_account/statement.html")

def transaction(request):
    transactions = Transaction.objects.all().order_by("-date")
    return render(request, "bankey_account/statement.html", {"transactions": transactions})


# make logout view

