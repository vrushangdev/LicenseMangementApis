from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('register_user/',views.register_user,name='userlogin'),
        path('login_user/',views.login_user,name='userlogin')

   ]
