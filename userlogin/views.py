from django.shortcuts import render,HttpResponse

# Create your views here.
def register_user(request):
    return render(request,'register.html')


def login_user(request):
    return render(request,'login.html')