from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import ugettext_lazy as _0

from django.core.validators import RegexValidator
phn_validator = RegexValidator(r"^[0-9]{10}$", "Phone number must be of 10 digits only consisting of number form 0-9.")

# Create your models here.  


class Student(AbstractUser):
    username = ''
    name = models.CharField(max_length = 30, blank = True)
    ph_no = models.IntegerField(validators=[phn_validator])
    roll_no = models.CharField(max_length = 11, primary_key=True)
    address = models.TextField()
    room_no = models.IntegerField()
    # username = roll_no
    USERNAME_FIELD = 'roll_no'
    REQUIRED_FIELDS = [ 'name']
    # objects = CustomUserManager()

    def __str__(self):
	    return self.name + self.roll_no

class Leave(models.Model):
    identity = models.ForeignKey("Student", on_delete = models.CASCADE, default = 1)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(default="no reason")
    status_accepted = models.BooleanField(default = False)

    def __str__(self):
        return "ID Number: " + str(self.identity.roll_no) +" | Status: "+ str(self.status_accepted)

# class Admin(AbstractUser):
#     identity = models.ForeignKey("User", on_delete = models.CASCADE)
#     isAdmin = models.BooleanField(default = True)
#     def __str__(self):
# 	    return self.name + self.roll_no

class Complaint(models.Model):
    identity = models.ForeignKey("Student", on_delete=models.CASCADE)
    # name_complaintant=models.TextField()
    description = models.TextField()
    type_of_complain = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    # room_no = models.IntegerField()

    def __str__(self):
        return str(self.identity.room_no) + " | Date: " + str(self.date) + " | Category: " + self.type_of_complain

class Notice(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
	    return self.heading
