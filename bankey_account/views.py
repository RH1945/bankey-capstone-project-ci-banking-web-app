from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Card, Transaction
from .forms import TransactionForm
from django.core.paginator import Paginator


@login_required
def account_view(request):
    cards = Card.objects.filter(account__user=request.user)
    return render(request, "bankey_account/account.html", {"cards": cards})


@login_required
def card_create_view(request):
    from django.forms import modelform_factory
    CardForm = modelform_factory(Card, fields=["account", "card_balance", "expiration_date", "card_type"])

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = CardForm()

    return render(request, "bankey_account/card_create.html", {"form": form})


@login_required
def statement_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)

    transactions = Transaction.objects.filter(
        sender=card.account.user
    ).order_by("-timestamp")

    paginator = Paginator(transactions, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        data = [
            {
                "sender": str(tx.sender),
                "receiver": str(tx.receiver),
                "amount": str(tx.amount),
                "reference": tx.reference,
                "timestamp": tx.timestamp.strftime("%Y-%m-%d %H:%M"),
            }
            for tx in page_obj
        ]
        return JsonResponse({"transactions": data, "has_next": page_obj.has_next()})

    return render(
        request,
        "bankey_account/statement.html",
        {
            "card": card,
            "page_obj": page_obj
        }
    )


@login_required
def transaction_create_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            tx = form.save(commit=False)
            tx.sender = request.user
            tx.save()
            return redirect("statement", card_number=card.card_number)
    else:
        form = TransactionForm()

    return render(
        request,
        "bankey_account/transaction.html",
        {"form": form, "card": card},
    )

def card_count_view(request):
    cards = Card.objects.filter(account__user=request.user)
    card_count = cards.count()

    return render(request, "bankey_account/account.html", {
        "cards": cards,
        "card_count": card_count
    })
