from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserForm  # Import the form for registration

# def index(request):
#     return render(request, "index.html")
def index(request):
    if request.user.is_authenticated:
        return redirect("/mainoffice/base")  # If logged in, go to mainoffice
    return render(request, "index.html")  # Else, show index page

def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CustomUserForm()
        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect("login_view")
            else:
                messages.error(request, "Registration failed. Please check your details.")
        return render(request, "register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/mainoffice/base")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/mainoffice/base")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("login_view")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("index")
