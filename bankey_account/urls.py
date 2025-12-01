from django.urls import path
from . import views

app_name = "bankey_account"

urlpatterns = [
    path("transaction/", views.make_transaction, name="make_transaction"),
    # add more paths here later
]
