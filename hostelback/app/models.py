from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from .managers import StudentManager

from django.core.validators import RegexValidator
phn_validator = RegexValidator(r"^[0-9]{10}$", "Phone number must be of 10 digits only consisting of number form 0-9.")

# Create your models here.  


class Student(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length = 30, blank = True)
    ph_no = models.IntegerField( validators=[phn_validator], null=True)
    roll_no = models.CharField(max_length = 11)
    address = models.TextField()
    room_no = models.IntegerField( null=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = StudentManager()

    def __str__(self):
        if self.is_staff == False:
	        return self.name + self.roll_no
        else:
            return "Adminstrator: " + self.email 

class Leave(models.Model):
    identity = models.ForeignKey("Student", on_delete = models.CASCADE, default = 1)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(default="no reason")
    status_accepted = models.BooleanField(default = False)

    def __str__(self):
        return "ID Number: " + str(self.identity.roll_no) +" | Status: "+ str(self.status_accepted)


class Complaint(models.Model):
    identity = models.ForeignKey("Student", on_delete=models.CASCADE)
    description = models.TextField()
    type_of_complain = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.identity.room_no) + " | Date: " + str(self.date) + " | Category: " + self.type_of_complain

class Notice(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
	    return self.heading