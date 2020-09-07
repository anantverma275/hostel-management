from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Student,Leave
# from .forms import StudentRegistrationForm

#bcs2018_007 salil1
#bcs2018_00 salil1

# Create your views here.
def signin(request):
    return render(request, "login.html")

def notice(request):
    return render(request,"notice.html")

def redisplay(request):
    return render(request,"base.html")

def dashboard(request):
    rollnumber = request.POST['rollnumber']
    password = request.POST['password']
    print(rollnumber, password)
    user = authenticate(request, username=rollnumber, password=password)
    if user is not None:
        print("User authenticated")
        login(request, user)
        return render(request,"base.html",{'uid': rollnumber})
    else:
        return HttpResponse("<h1> hag diya </h1>")


# def dashboard(request):
#     return render(request, "dashboard.html")

def leave(request):
    # this function is used to just render the page leave.html
    print(request.user)
    return render(request, "leave.html")

def apply_leave(request):
    # this function accepts the parameters and data for leave application and saves it to database
    print(request.user)
    if (request.method == "POST"):
        if request.POST.get("address"):print("address sahi")
        if request.POST.get("phn"):print("phn sahi")
        if request.POST.get("reason"):print("reason sahi")
        if request.POST.get("strt_date"):print("strt_date sahi")
        if request.POST.get("end_date"):print("end_date sahi")
        if  request.POST.get("address") and request.POST.get("phn") and request.POST.get("reason") and request.POST.get("strt_date") and request.POST.get("end_date"):
            print("leave application ki request aayi")
            # now we fill relevant leave parameters 
            appn=Leave()
            appn.applicant=request.user
            appn.address_to_go=request.POST.get("address")
            appn.start_date=request.POST.get("strt_date")
            appn.end_date=request.POST.get("end_date")
            appn.reason=request.POST.get("Reason")
            appn.save()
            return HttpResponse("<h1> Application for leave placed </h1>")
        # form = StudentRegistrationForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     form.save()
        #     print("succesS")
        else:
            return HttpResponse("<h1> sahi se bharle </h1>")
        # return render(request, "leave.htm")

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


