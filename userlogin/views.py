from django.shortcuts import render,HttpResponse

# Create your views here.
def register_user(request):
    return render(request,'userlogin/base.html')