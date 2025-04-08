from django.shortcuts import render

# Create your views here.

def books(request):
    return render(request,"books.html")

def catalog(request):
    return render(request, 'catalog.html')

# Membership page view (Information about membership, sign-up, etc.)
def membership(request):
    return render(request, 'membership.html')

# Library Events page view (Upcoming events, schedules, etc.)
def library_events(request):
    return render(request, 'library-events.html')

# Contact page view (Contact details or form)
