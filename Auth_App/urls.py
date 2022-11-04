
from django.contrib import admin
from django.urls import path, include
from Auth_App import views

urlpatterns = [
     path('login/',views.user_login),
     path('register/',views.user_register),
     path('index/',views.index),
     path('logout/',views.logout)
]
