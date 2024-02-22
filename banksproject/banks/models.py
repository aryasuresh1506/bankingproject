from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

    def __str__(self):
        return self.username

class Branches(models.Model):
    DISTRICT_CHOICE = [
        ('Idukki', 'Idukki'),
        ('Kottayam', 'Kottayam'),
        ('Kollam', 'Kollam'),
        ('Vayanad', 'Vayanad'),
        ('Eranakulam', 'Eranakulam'),
    ]
    branch=models.CharField(max_length=250)
    district=models.CharField(max_length=250,choices=DISTRICT_CHOICE)

    def __str__(self):
        return self.branch

class Forum(models.Model):
    GENDER_CHOICE=[
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]
    AC_CHOICE=[
        ('S', 'Savings Account'),
        ('C', 'Current Account'),
    ]
    username=models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=25)
    dob = models.DateField(null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE,null=True)
    phoneno = models.IntegerField(null=True)
    email = models.EmailField(max_length=20, primary_key=True)
    address = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=50,null=True)
    branch = models.CharField(max_length=50,null=True)
    accounttype = models.CharField(max_length=10,choices=AC_CHOICE)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.username

