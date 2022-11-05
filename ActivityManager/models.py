from django.db import models
from Auth_App.models import Student

class Club(models.Model):
    club_id = models.IntegerField(primary_key = True)
    club_name = models.CharField(max_length=100)
    club_adminId = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name
