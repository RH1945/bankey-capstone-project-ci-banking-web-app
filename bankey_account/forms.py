from django import forms
from .models import Transaction, BankeyAccount, Card


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["receiver", "amount"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs.update({
            "min": "1.00",
            "step": "0.01",
        })

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount is not None and amount <= 0:
            raise forms.ValidationError("Amount must be positive.")
        return amount


class BankeyAccountForm(forms.ModelForm):
    class Meta:
        model = BankeyAccount
        fields = ["acc_type", "currency"]


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["card_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["card_type"].choices = Card.PERSONAL_CARD_TYPE
