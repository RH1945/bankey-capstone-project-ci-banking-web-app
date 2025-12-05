from django.shortcuts import render, redirect
from django.contrib.auth import logout


def dashboard(request):
    return render(request, "dashboard/index.html")


def login_view(request):
    return render(request, "dashboard/log_in.html")


def signup_view(request):
    return render(request, "dashboard/sign_up.html")


def logout_view(request):
    logout(request)
    return redirect("dashboard")
