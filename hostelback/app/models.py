from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator
phn_validator = RegexValidator(r"^[0-9]{10}$", "Phone number must be of 10 digits only.")

# Create your models here.


class Student(AbstractUser):
    name = models.CharField(max_length = 30, blank = True)
    ph_no = models.IntegerField(validators=phn_validator)
    roll_no = models.CharField(max_length = 10, unique = True)
    address = models.TextField()
    room_no = models.IntegerField() 

    def __str__(self):
	    return self.name + self.roll_no

class Leave(models.Model):
    applicant = models.ForeignKey("Student", on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status_accepted = models.BooleanField(default = False)

    def __str__(self):
	    return "ID Number: " + self.applicant.roll_no +" | Status: "+ self.status_accepted

class Complaint(models.Model):
    description = models.TextField()
    type = models.CharField()
    date = models.DateField(auto_now_add=True)
    room_no = models.IntegerField()

    def __str__(self):
        return self.room_no + " | Date: " + self.date

class Notice(models.Model):
    content = models.TextField()
    heading = models.CharField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
	    return self.heading