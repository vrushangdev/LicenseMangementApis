from django.shortcuts import render,HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse("<h1>Blog Will Be Added Here</h1>")

def landing_page(request):
    return HttpResponse("<h1>Here Goes Landing Page </h1>")