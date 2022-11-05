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
        for i in range(0,len(activities)):
            for j in range(i,len(activities)):
                if(activities[i].date_time > activities[j].date_time):
                    activities[i],activities[j] = activities[j],activities[i]
        return render(request, 'home.html',{'User':request.user,'Activities':activities})
    else:
        return redirect(v.user_login)