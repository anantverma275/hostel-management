from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def signin(request):
    return render(request, "login.html")

def verify(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        print("User authenticated")
        login(request, user)
        redirect("dashboard")
    else:
        return HttpResponse("<h1> hag diya </h1>")


def dashboard(request):
    return render(request, "dashboard.html")