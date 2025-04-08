from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request,"categories.html")

def fiction(request):
    return render(request, "fiction.html")

# Membership page view (Information about membership, sign-up, etc.)
def Non_fiction(request):
    return render(request, "Non_fiction.html")

# Library Events page view (Upcoming events, schedules, etc.)
def Comics(request):
    return render(request, "Comics.html")

def Romance(request):
    return render(request, "Romance.html")

