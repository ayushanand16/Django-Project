from django.shortcuts import render, HttpResponse, redirect
from .models import Branch, Hostel,Student
from django.contrib.auth.models import User, auth
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from ActivityManager import views as v




# Create your views here.




    

def user_login(request):
    if request.user.is_authenticated :
        return redirect(v.home)
    if request.method == 'POST':
        username = request.POST['roll']
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(v.home)
        else:
            return HttpResponse('Wrong Credentials')
    else:
        return render(request, 'login.html')


    


def user_register(request):
    if request.user.is_authenticated :
        return redirect(v.home)
    if request.method == 'POST':
        branch=Branch.objects.get(branch_id=request.POST['branch'])
        #print(branch)
        first_name=request.POST['fname']
        #print(first_name)
        last_name=request.POST['lname']
        roll=request.POST['roll']
        hostel=Hostel.objects.get(hostel_id=request.POST['hostel'])
        room=request.POST['room']
        phone=request.POST['phone']
        email=request.POST['email']
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=roll, password=password, first_name=first_name, last_name=last_name, email=email)
            if user:
                user.save()
                student = Student(name=first_name+' '+last_name,roll_no=roll,branch=branch,email=email,hostel=hostel,room_no=room,phone_number=phone)
                student.save()
                #print(student)
        except IntegrityError:
            return HttpResponse('Username taken')
        except :
             redirect('/')
    branch = Branch.objects.all()
    hostel = Hostel.objects.all()
    context = {'branch':branch,'hostel':hostel}
    return render(request,'Register.html',context)


def logout(request):
    auth.logout(request)
    return redirect(user_login)


