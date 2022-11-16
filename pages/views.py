from django.shortcuts import render

def index(request):
    user = 'Sign In'
    if request.user.is_authenticated:
        user = request.user.first_name+' '+request.user.last_name
    return render(request, 'landing.html',{'user':user})