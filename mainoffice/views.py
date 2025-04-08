
from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login_view")
def base(request):
    return render(request,"base.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def privacy_policy(request):
    return render(request,"privacy_policy.html")
def terms(request):
    return render(request,"terms.html")