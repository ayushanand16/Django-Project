from django.shortcuts import render, HttpResponse, redirect
from .models import Branch, Hostel,Student
from django.contrib.auth.models import User, auth
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError




# Create your views here.


def index(request):
    if request.user.is_authenticated :
        return HttpResponse('Welcome '+request.user.username)
    else:
        return redirect(user_login)

    

def user_login(request):
    if request.user.is_authenticated :
        return redirect(index)
    if request.method == 'POST':
        username = request.POST['roll']
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
        else:
            return HttpResponse('Wrong Credentials')
    else:
        return render(request, 'login.html')


    


def user_register(request):
    if request.user.is_authenticated :
        return redirect(index)
    if request.method == 'POST':
        # branch=request.POST['branch']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        roll=request.POST['roll']
        # hostel=request.POST['hostel']
        room=request.POST['room']
        phone=request.POST['phone']
        email=request.POST['email']
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=roll, password=password, first_name=first_name, last_name=last_name, email=email)
            if user:
                user.save()
                return redirect("/")
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


