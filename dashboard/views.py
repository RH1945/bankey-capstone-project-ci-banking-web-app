from django.shortcuts import render, redirect
from django.contrib.auth import logout
from bankey_account.models import Card


def dashboard(request):
    card_count = Card.objects.count()
    return render(request, "dashboard/index.html", {
        "card_count": card_count
    })


def login_view(request):
    return render(request, "dashboard/log_in.html")


def signup_view(request):
    return render(request, "dashboard/sign_up.html")


def logout_view(request):
    logout(request)
    return redirect("dashboard")
