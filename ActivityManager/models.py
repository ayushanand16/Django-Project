from django.db import models
from Auth_App.models import Student
from django.contrib.auth.models import User

class Venue(models.Model):
    venue_Id = models.IntegerField(primary_key=True)
    venue_name = models.CharField(max_length=100)


    def __str__(self):
        return self.venue_name

class Club(models.Model):
    club_id = models.IntegerField(primary_key = True)
    club_name = models.CharField(max_length=100)
    club_adminId = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name


class Club_Student_List(models.Model):
    club = models.ForeignKey('Club', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Activity(models.Model):
    Club = models.ForeignKey('Club',on_delete=models.CASCADE)
    Venue = models.ForeignKey('Venue',on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    act = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.title,self.date_time)

class SelfActivtiy(models.Model):
    Student = models.ForeignKey(Student,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    act = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.title,self.date_time) 


class Theme(models.Model):
    theme = models.BooleanField(default=True)

class ProPic(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    propic = models.ImageField(upload_to="propic/images",default="")
