from django.shortcuts import render, HttpResponse, redirect
from Auth_App import views as v

def home(request):
    if request.user.is_authenticated :
        return render(request, 'home.html',{'User':request.user})
    else:
        return redirect(v.user_login)