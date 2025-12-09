from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Card, Transaction, BankeyAccount
from .forms import TransactionForm, BankeyAccountForm, CardCreateForm
from .utils import generate_expiration_date
from datetime import date
from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint


@login_required
def statement_pdf_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)
    transactions = Transaction.objects.filter(sender=card.account.user)

    html = get_template("bankey_account/statement_pdf.html").render({
        "card": card,
        "transactions": transactions
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "filename=statement.pdf"

    weasyprint.HTML(string=html).write_pdf(response)
    return response


@login_required
def account_view(request):
    account = BankeyAccount.objects.filter(user=request.user).first()

    if not account:
        return redirect("bankey_account:account_create")

    cards = Card.objects.filter(account=account)

    return render(request, "bankey_account/account.html", {
        "account": account,
        "cards": cards
    })


@login_required
def account_create_view(request):
    if BankeyAccount.objects.filter(user=request.user).exists():
        return redirect("bankey_account:account")

    if request.method == "POST":
        form = BankeyAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect("bankey_account:card_create")
    else:
        form = BankeyAccountForm()

    return render(request, "bankey_account/account_create.html", {"form": form})


@login_required
def card_create_view(request):
    account = BankeyAccount.objects.filter(user=request.user).first()

    if not account:
        return redirect("bankey_account:account")

    if request.method == "POST":
        form = CardCreateForm(request.POST)

        if form.is_valid():
            card = form.save(commit=False)
            card.account = account
            card.expiration_date = generate_expiration_date()
            card.save()
            return redirect("bankey_account:account")

    else:
        form = CardCreateForm()

    return render(
        request,
        "bankey_account/card_create.html",
        {"form": form}
    )


@login_required
def statement_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)

    transactions = Transaction.objects.filter(
        sender=card.account.user
    ).order_by("-timestamp")

    paginator = Paginator(transactions, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "bankey_account/statement.html", {
        "card": card,
        "page_obj": page_obj
    })


@login_required
def transaction_create_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            tx = form.save(commit=False)
            tx.sender = request.user
            tx.save()
            return redirect("bankey_account:statement", card_number=card.card_number)
    else:
        form = TransactionForm()

    return render(request, "bankey_account/transaction.html", {
        "form": form,
        "card": card
    })
