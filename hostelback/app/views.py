from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Student,Leave,Complaint
from django.contrib.auth.decorators import login_required
# from .forms import StudentRegistrationForm

#bcs2018_007 salil1
#bcs2018_00 salil1

# Create your views here.

def land(request):
    return render(request, "login.html")

def login_req(request):
    if (request.method == "POST"):
        print("request aai")
        rollnumber = request.POST.get('rollnumber')
        password = request.POST.get('password')
        print(rollnumber, password)
        user = authenticate(request, username=rollnumber, password=password)
        if user is not None:
            print("User authenticated, username:")
            login(request, user)
            print(request.user.name, request.user.roll_no)
            return redirect('dashboard')
        else:
            return render(request, "login.html")

def notice_stud(request):
    return render(request,"notice_stud.html")

def redisplay(request):
    return render(request, "navigation_user.html", {"user": request.user})


@login_required
def dashboard(request):
    print(request.user)
    return render(request, "navigation_user.html", {"user": request.user})


@login_required
def leave(request):
    # this function is used to just render the page leave.html
    # print(request.user)
    return render(request, "apply_leave_stud.html")

def leave_req(request):
    # this function accepts the parameters and data for leave application and saves it to database
    print(request.user)
    if (request.method == "POST"):
        if request.POST.get("reason") and request.POST.get("strt_date") and request.POST.get("end_date") :
            # print("leave application ki request aayi")
            # now we fill relevant leave parameters 
            leave_obj=Leave()
            leave_obj.identity = request.user
            leave_obj.start_date=request.POST.get("strt_date")
            leave_obj.end_date=request.POST.get("end_date")
            leave_obj.reason=request.POST.get("reason")
            leave_obj.save()
            return redirect("dashboard")
        else:
            return HttpResponse(request, "apply_leave_stud.html")
        # return render(request, "leave.htm")
@login_required
def complaint(request):
    return render(request, "apply_complaint_stud.html")

def complaint_req(request):
    if (request.method == "POST"):
        if request.POST.get("category") and request.POST.get("desc"):
            print("complaint ki request aayi")
            cmpl=Complaint()
            cmpl.identity = request.user
            # cmpl.name_complaintant = request.POST.get("request.user.name")
            # cmpl.room_no = request.POST.get("request.user.room_no")
            cmpl.type_of_complain = request.POST.get("category")
            cmpl.description = request.POST.get("desc")
            cmpl.save()
            return redirect("dashboard")
        else:
            return HttpResponse("compaint")

# admin views functions

def login_req_admin(request):
    if (request.method == "POST"):
        print("request aai")
        username = request.POST.get('UserName')
        password = request.POST.get('password_admin')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if username=="admin" and password=="password":
            return HttpResponse("<h1> welcome admin </h1>")
        else:
            return HttpResponse("<h1> wrong username or password </h1>")
        # if user is not None:
        #     print("User authenticated, username:")
        #     login(request, user)
        #     print(request.user.name, request.user.roll_no)
        #     return redirect('dashboard_admin')
        

@login_required
def dashboard_admin(request):
    print(request.user)
    return render(request, "navigation_admin.html", {"user": "admin"})





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
            return redirect('land')
        # form = StudentRegistrationForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     form.save()
        #     print("succesS")
    else:
        return render(request, "register.html")


