from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    branch_id = models.IntegerField(primary_key = True)

    def __str__(self):
        return self.branch_name


class Hostel(models.Model):
    hostel_id = models.IntegerField(primary_key = True)
    hostel_name = models.CharField(max_length=50)

    def __str__(self):
        return self.hostel_name


class Student(models.Model):
    name = models.CharField(max_length=50)
    #avatar=models.ImageField(upload_to='pics',blank=True)
    roll_no = models.IntegerField(primary_key=True)
    branch = models.ForeignKey('Branch',on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    hostel = models.ForeignKey('Hostel',on_delete=models.CASCADE)
    room_no = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, default='+91') # Validators should be a list
    def __str__(self):
        return "{} {}".format(self.roll_no, self.name)




