from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Student, Leave, Complaint, Notice
from django.contrib.auth.decorators import login_required

# Create your views here.

def land(request):
    return render(request, "login_stud.html")

def login_req(request):
    if (request.method == "POST"):
        print("request aai")
        rollnumber = request.POST.get('rollnumber')
        email= rollnumber[:3] + "_" + rollnumber[3:7] + rollnumber[8:].lstrip("0") + "@iiitm.ac.in"
        password = request.POST.get('password')
        print(rollnumber, password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("User authenticated, username:")
            login(request, user)
            print(request.user.name, request.user.roll_no)
            return redirect('dashboard')
        else:
            return render(request, "login_stud.html")

def notice_stud(request):
    notice_lis = Notice.objects.all()
    return render(request, "notice_stud.html", {'not_lis': notice_lis})

@login_required
def dashboard(request):
    leave_applications = Leave.objects.filter(identity=request.user)
    return render(request, "base.html", {"user": request.user, 'all_appns': leave_applications})

@login_required
def leave(request):
    return render(request, "leave.html")

@login_required
def leave_req(request):
    print(request.user)
    if (request.method == "POST"):
        if request.POST.get("reason") and request.POST.get("strt_date") and request.POST.get("end_date") :
            leave_obj=Leave()
            leave_obj.identity = request.user
            leave_obj.start_date=request.POST.get("strt_date")
            leave_obj.end_date=request.POST.get("end_date")
            leave_obj.reason=request.POST.get("reason")
            leave_obj.save()
            return redirect("dashboard")
        else:
            return HttpResponse(request, "leave.html")

@login_required
def complaint(request):
    return render(request, "complaint.html")

@login_required
def complaint_req(request):
    if (request.method == "POST"):
        if request.POST.get("category") and request.POST.get("desc"):
            print("complaint ki request aayi")
            cmpl=Complaint()
            cmpl.identity = request.user
            cmpl.type_of_complain = request.POST.get("category")
            cmpl.description = request.POST.get("desc")
            cmpl.save()
            return redirect("dashboard")
        else:
            return HttpResponse("compaint")

def register(request):
    if (request.method == "POST"):
        if request.POST.get("name") and request.POST.get("roll_no") and request.POST.get("phn") and request.POST.get("room_no") and request.POST.get("address") and request.POST.get("password"):
            print("Request aai")
            std = Student()
            std.email = request.POST.get("roll_no")[:3] + "_" + request.POST.get("roll_no")[3:7] + request.POST.get("roll_no")[8:].lstrip("0") + "@iiitm.ac.in"
            std.name = request.POST.get("name")
            std.roll_no = request.POST.get("roll_no")
            std.ph_no = request.POST.get("phn")
            std.room_no = request.POST.get("room_no")
            std.address = request.POST.get("address")
            std.set_password(request.POST.get("password"))
            std.save()
            return redirect('land')
    else:
        return render(request, "register.html")


@login_required
def occupant(request):
    stud_occupant = Student.objects.filter(is_superuser=False)
    return render(request, "occupants_Student.html", {'studs': stud_occupant})
