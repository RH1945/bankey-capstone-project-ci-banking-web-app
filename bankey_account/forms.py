from django import forms
from .models import Transaction, BankeyAccount, Card


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["card", "receiver", "amount"]
        labels = {
            "card": "From card",
            "receiver": "Sending to",
            "amount": "Amount",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        self.fields["card"].queryset = Card.objects.filter(account__user=user)
        self.sender = user

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount is not None and amount <= 0:
            raise forms.ValidationError("Amount must be positive.")
        return amount

    def clean(self):
        cleaned = super().clean()

        card = cleaned.get("card")
        receiver = cleaned.get("receiver")
        amount = cleaned.get("amount")

        if not card or not amount or receiver is None:
            return cleaned

        if receiver == self.sender:
            raise forms.ValidationError("Sender and receiver must be different.")

        if card.card_balance < amount:
            raise forms.ValidationError(
                f"Insufficient funds. Your card balance is {card.card_balance}."
            )

        return cleaned


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
