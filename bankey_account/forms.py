from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["receiver", "amount"]   # sender is NOT shown to user because it's themselves
