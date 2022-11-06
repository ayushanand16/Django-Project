from django.shortcuts import render, HttpResponse, redirect
from Auth_App import views as v
from Auth_App.models import Student, Hostel
from .models import Activity, Club_Student_List, Venue, Club, SelfActivtiy
from django.contrib.auth.decorators import login_required
import datetime

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
        return render(request, 'home.html',{'User':request.user,'Activities':activities,'now':datetime.date.today()})
    else:
        return redirect(v.user_login)

def create(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            club = request.POST['club']
            title=request.POST['title']
            act=request.POST['act']
            venue=request.POST['venue']
            datetime=request.POST['date']
            if club == 'self':
                student = Student.objects.get(roll_no=request.user.username)
                selfact = SelfActivtiy(Student=student,title=title,act=act,date_time=datetime)
                selfact.save()
                return redirect(self)
            else :
                club_of_activity = Club.objects.get(club_id=club)
                venue_of_activity = Venue.objects.get(venue_Id=venue)
                clubact = Activity(Club=club_of_activity,title=title,act=act,date_time=datetime,Venue=venue_of_activity)
                clubact.save()
                return redirect(home)
            
        else :
            venues = Venue.objects.all()
            student = Student.objects.get(roll_no=request.user.username)
            clubs = Club.objects.filter(club_adminId=student)
            return render(request,'create.html',{'venues':venues,'clubs':clubs})

    else:
        return redirect(v.user_login)

def self(request):
    if request.user.is_authenticated :
        student = Student.objects.get(roll_no=request.user.username)
        selfacts = SelfActivtiy.objects.filter(Student=student).order_by('date_time')
        return render(request,'self.html',{'selfacts':selfacts,'User':request.user,'now':datetime.date.today()})
    else:
        return redirect(v.user_login)

def profile(request):
    if request.user.is_authenticated :
        student = Student.objects.get(roll_no=request.user.username)
        return render(request,'profiles.html',{'user':student})
    else :
        return redirect(v.user_login)

def edit(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            hostel = Hostel.objects.get(hostel_id=request.POST['hostel'])
            room_no = request.POST['room']
            phone = request.POST['phone']
            email = request.POST['email']
            student = Student.objects.get(roll_no=request.user.username)
            student.hostel = hostel
            student.room_no = room_no
            student.phone_number = phone
            student.email = email
            student.save()
            return redirect(profile)
        else :
            student = Student.objects.get(roll_no=request.user.username)
            hostel = Hostel.objects.all()
            return render(request,'edit.html',{'user':student,'hostel':hostel})