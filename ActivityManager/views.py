from django.shortcuts import render, HttpResponse, redirect
from Auth_App import views as v
from Auth_App.models import Student
from .models import Activity, Club_Student_List 

def home(request):
    if request.user.is_authenticated :
        student = Student.objects.get(roll_no=request.user.username)
        print(student)
        clubs = Club_Student_List.objects.filter(student=student)
        print(clubs)
        activities = []
        for club in clubs :
            activity = Activity.objects.filter(Club=club.club)
            for act in activity :
                activities.append(act)
        print(activities)
        activities.sort(key=lambda x: x.date_time)
        return render(request, 'home.html',{'User':request.user,'Activities':activities})
    else:
        return redirect(v.user_login)