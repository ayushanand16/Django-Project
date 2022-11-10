
from django.contrib import admin
from django.urls import path, include
from Auth_App import views

urlpatterns = [
     path('login/',views.user_login, name='login'),
     path('register/',views.user_register, name='register'),
     path('logout/',views.logout, name='logout')
]
