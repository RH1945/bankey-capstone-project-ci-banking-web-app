from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Card, Transaction, BankeyAccount
from .forms import TransactionForm, BankeyAccountForm, CardCreateForm
from .utils import generate_expiration_date
from django.db.models import Q


# ACCOUNT DASHBOARD
@login_required
def account_view(request):
    account = BankeyAccount.objects.filter(user=request.user).first()

    if not account:
        return redirect("bankey_account:account_create")

    cards = Card.objects.filter(account=account)
    primary_card = cards.first()  # Used for nav display

    return render(request, "bankey_account/account.html", {
        "account": account,
        "cards": cards,
        "primary_card": primary_card,
    })


# CREATE BANK ACCOUNT
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


# CREATE CARD
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

            # Initial balance so demo works nicely
            card.card_balance = 200
            card.save()

            # Update account total balance
            account.update_balance()

            messages.success(request, "New card created successfully!")
            return redirect("bankey_account:account")

    else:
        form = CardCreateForm()

    return render(
        request,
        "bankey_account/card_create.html",
        {"form": form}
    )


# STATEMENT VIEW
@login_required
def statement_view(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)
    account = card.account
    cards = Card.objects.filter(account=account)
    primary_card = card

    transactions = Transaction.objects.filter(
        Q(sender=card.account.user) | Q(receiver=card.account.user)
    ).order_by("-timestamp")

    paginator = Paginator(transactions, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        data = {
            "transactions": [
                {
                    "reference": tx.reference,
                    "sender": str(tx.sender),
                    "receiver": str(tx.receiver),
                    "amount": float(tx.amount),
                    "timestamp": tx.timestamp.strftime("%Y-%m-%d %H:%M"),
                    "direction": "out" if tx.sender == request.user else "in",
                }
                for tx in page_obj
            ],
            "has_next": page_obj.has_next(),
        }
        return JsonResponse(data)

    return render(request, "bankey_account/statement.html", {
        "card": card,
        "page_obj": page_obj,
        "account": account,
        "cards": cards,
        "primary_card": primary_card,
    })


@login_required
def transaction_create_view(request):
    cards = Card.objects.filter(account__user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)

        if form.is_valid():
            tx = form.save(commit=False)

            sender_card = form.cleaned_data["card"]
            amount = form.cleaned_data["amount"]
            receiver_user = form.cleaned_data["receiver"]
            reference = form.cleaned_data.get("reference", "")

            if amount <= 0:
                return JsonResponse({"success": False, "error": "Amount must be positive."})

            if sender_card.card_balance < amount:
                return JsonResponse({"success": False, "error": "Insufficient funds."})

            # update balance for sending party
            sender_card.card_balance -= amount
            sender_card.save()
            sender_card.account.update_balance()

            # update balance for receving
            receiver_card = Card.objects.filter(account__user=receiver_user).first()
            if receiver_card:
                receiver_card.card_balance += amount
                receiver_card.save()
                receiver_card.account.update_balance()

            # save transaction
            tx.sender = request.user
            tx.reference = reference
            tx.save()

            # ajax response
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "card": sender_card.card_number,
                    "receiver": f"{receiver_user.first_name} {receiver_user.last_name}",
                    "amount": float(amount),
                    "reference": reference,
                    "date": tx.timestamp.strftime("%Y-%m-%d %H:%M"),
                })

            # fallback for normal POST (just in case)
            messages.success(request, "Transaction completed successfully!")
            return redirect("bankey_account:account")

        else:
            # Form invalid
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": form.errors.as_text()})

            messages.error(request, "Invalid transaction.")
            return redirect("bankey_account:transaction")

    # GET request
    form = TransactionForm(user=request.user)
    return render(request, "bankey_account/transaction.html", {
        "form": form,
        "cards": cards
    })

@login_required
def card_delete_view(request, card_id):
    card = get_object_or_404(Card, id=card_id, account__user=request.user)
    # This view unlinks the card but keeps transactions, we also return a message to confirm card has been deleted
    if request.method == "POST":
        Transaction.objects.filter(card=card).update(card=None)
        card.delete()
        card.account.update_balance()
        messages.success(request, "Card deleted successfully.")
        return redirect("bankey_account:account")
    return redirect("bankey_account:account")

