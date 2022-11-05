from django.shortcuts import render, HttpResponse, redirect
from Auth_App import views as v

def home(request):
    if request.user.is_authenticated :
        return HttpResponse('Welcome '+request.user.username)
    else:
        return redirect(v.user_login)