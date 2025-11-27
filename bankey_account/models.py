from django.db import models

# Create your models here.

CARD_TYPE = ((0, "Debit"), (1, "Credit"))


class BankeyAccount(models.Model):
    """
    Creates an instance of bankey_account of a type (Current, Savings, Business and Joint)
    It saves data such as its users' Name and email, Balance, Type, Acc Number, User
    Related to user
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    balance = models.FloatField()
    account_type = models.IntegerField()
    acc_number = models.CharField(max_length=32)


# that can be
#    used to create new cards and thus access to transactions, loans, benefits, etc.


class Card(models.Model):
    """
    Creates an instance of card of a type (Debit, Credit) related to :model:`BankeyAccount`
    """
    type = models.IntigerField(choices=CARD_TYPE, default=0)


    ## METHOD TO INCREASE OR DECREASE THE BALANCE = TRANSACTION

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.first_name, self.last_name} | written by {self.author}"  ????????
