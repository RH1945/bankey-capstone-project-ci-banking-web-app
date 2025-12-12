from bankey_account.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def dashboard(request):
    return render(request, "dashboard/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful. Welcome back!")
            return redirect("bankey_account:account_create")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "dashboard/log_in.html")


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        dob = request.POST.get("dob")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Password check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("dashboard:signup")

        # User uniqueness checks
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("dashboard:signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("dashboard:signup")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
        )

        # Optional DOB field
        user.dob = dob
        user.save()

        # Auto-login
        login(request, user)
        messages.success(request, "Signup successful! Welcome to Bankey.")
        return redirect("bankey_account:account_create")

    return render(request, "dashboard/sign_up.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect("dashboard:dashboard")
