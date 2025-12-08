from django import forms
from .models import Transaction, BankeyAccount, Card



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["receiver", "amount"]


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