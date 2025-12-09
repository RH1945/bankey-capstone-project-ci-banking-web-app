from django.urls import path
from . import views

app_name = "bankey_account"

urlpatterns = [
    path("", views.account_view, name="account"),
    path("account/create/", views.account_create_view, name="account_create"),
    path("card/create/", views.card_create_view, name="card_create"),
    # path("statement/<str:card_number>/pdf/", views.statement_pdf_view, name="statement_pdf"),
    path("statement/<str:card_number>/", views.statement_view, name="statement"),
    path("transaction/<str:card_number>/", views.transaction_create_view, name="transaction"),
]
