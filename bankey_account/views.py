from django.shortcuts import render, redirect
from .forms import TransactionForm

# Create your views here.

def make_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.sender = request.user  # 👈 logged-in user
            transaction.save()
            return redirect("dashboard")
    else:
        form = TransactionForm()

    return render(request, "transaction.html", {"form": form})
