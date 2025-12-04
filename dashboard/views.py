from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def login_view(request):
    return render(request, "dashboard/log_in.html")

def signup_view(request):
    return render(request, "dashboard/sign_up.html")

def logout_view(request):
    return HttpResponse("Logged out")

