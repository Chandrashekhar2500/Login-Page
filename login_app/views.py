from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
# Create your views here.


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def SignUpView(request):
    
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account created successfully !!")
            fm.save()
    else:
        fm = UserCreationForm

    return render(request,'registration/signup.html',{"form":fm})


def hello(request):
   return render(request, "hello.html", {})