from msilib.schema import ListView

from django.db import transaction
from .models import Transaction

from django.shortcuts import render

# Create your views here.


class TransactionListView(ListView):
    '''
    Conduit for displaying transactions as a list with important information related to :models:`Transaction`
    '''
