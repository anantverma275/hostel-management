from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Student
# from .forms import StudentRegistrationForm

# Create your views here.
def signin(request):
    return render(request, "login.html")

def dashboard(request):
    rollnumber = request.POST['rollnumber']
    password = request.POST['password']
    print(rollnumber, password)
    user = authenticate(request, username=rollnumber, password=password)
    if user is not None:
        print("User authenticated")
        login(request, user)
        return render(request,"d_temp.html")
    else:
        return HttpResponse("<h1> hag diya </h1>")


# def dashboard(request):
#     return render(request, "dashboard.html")

def leave(request):
    return render(request, "leave.html")

def complaint(request):
    return render(request, "complaint.html")

def profile_change(request):
    return HttpResponse("<h1> profile change walla page aayega yahan </h1>")

def register(request):
    if (request.method == "POST"):
        if request.POST.get("name") and request.POST.get("roll_no") and request.POST.get("phn") and request.POST.get("room_no") and request.POST.get("address") and request.POST.get("password"):
            print("Request aai")
            std = Student()
            std.name = request.POST.get("name")
            std.roll_no = request.POST.get("roll_no")
            std.ph_no = request.POST.get("phn")
            std.room_no = request.POST.get("room_no")
            std.address = request.POST.get("address")
            std.set_password(request.POST.get("password"))
            std.save()
            return redirect('signin')
        # form = StudentRegistrationForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     form.save()
        #     print("succesS")
    else:
        return render(request, "register.html")


