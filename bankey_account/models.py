# Format Python code here
from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from .utils import (
    generate_account_number,
    generate_card_number,
    generate_expiration_date,
)

# Create your models here.

ACCOUNT_TYPE = ((0, "Personal"), (1, "Business"), (2, "No account"))
CURRENCY_CHOICES = (
    ("GBP", "British Pound"),
    ("EUR", "Euro"),
    ("USD", "US Dollar"),
)


class User(AbstractUser):
    full_name = models.CharField(max_length=64, editable=False)
    dob = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} | {self.last_name} | {self.email}"


class BankeyAccount(models.Model):
    """
    Creates an instance of BankeyAccount of a type (Personal or Business)
    It saves its users' full name and email, and the accounts Balance, Type, and Number.
    Related to :model:`User`
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acc_balance = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    acc_type = models.IntegerField(choices=ACCOUNT_TYPE, default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    acc_number = models.CharField(max_length=32, unique=True, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="GBP")

    def save(self, *args, **kwargs):
        if not self.acc_number:
            self.acc_number = generate_account_number(self.user.dob)
        super().save(*args, **kwargs)

    def is_personal(self):
        return self.acc_type == 0

    def is_business(self):
        return self.acc_type == 1

    def __str__(self):
        return f"{self.user.full_name} | {self.acc_type} | {self.acc_number}"

    def update_balance(self):
        total = sum(card.card_balance for card in self.card_set.all())
        self.acc_balance = total
        self.save(update_fields=["acc_balance"])

    class Meta:
        ordering = ["created_on"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class Card(models.Model):
    """
    Creates an instance of card of a type (Debit, Credit) related to :model:`BankeyAccount`
    """

    PERSONAL_CARD_TYPE = ((0, "Debit"), (1, "Credit"))
    BUSINESS_CARD_TYPE = ((0, "Company"), (1, "Wage-Payment"))

    account = models.ForeignKey(BankeyAccount, on_delete=models.CASCADE)
    card_balance = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    expiration_date = models.DateField(default=generate_expiration_date)
    card_number = models.CharField(
        max_length=16, unique=True, default=generate_card_number
    )
    card_type = models.IntegerField(choices=PERSONAL_CARD_TYPE)
    created_on = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.expiration_date < date.today()

    def __str__(self):
        return f"{self.account.user.full_name} | {self.card_number}"

    def clean(self):
        if not self.account_id:
            return

        if self.account.acc_type == 0:  # Personal
            valid = dict(self.PERSONAL_CARD_TYPE).keys()
        else:  # Business
            valid = dict(self.BUSINESS_CARD_TYPE).keys()

        if self.card_type not in valid:
            raise ValidationError("Invalid card type for this account type.")

    class Meta:
        ordering = ["created_on"]
        verbose_name = "Card"
        verbose_name_plural = "Cards"


class Transaction(models.Model):
    """
    Creates an instance of Transaction related to :model:`BankeyAccount`
    """

    reference = models.CharField(max_length=24, blank=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_transactions",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_transactions",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey("Card", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.sender} → {self.receiver} | {self.amount}"

    class Meta:
        ordering = ["timestamp"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def clean(self):
        from django.core.exceptions import ValidationError

        sender = getattr(self, "sender", None)
        receiver = getattr(self, "receiver", None)

        if sender is not None and receiver is not None:
            if sender == receiver:
                raise ValidationError("Sender and receiver cannot be the same.")
