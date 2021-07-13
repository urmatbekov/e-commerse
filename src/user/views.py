from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout

UserCreationForm._meta.model = User

# Create your views here.
def register(request):
    registerForm = UserCreationForm()

    if request.method == "POST":
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'You are success registered')
            return redirect("home_page")
    
    return render(request,"users/register.html",{"form":registerForm})

def authentication(request):
    authForm = AuthenticationForm()
    
    if request.method == "POST":
        authForm = AuthenticationForm(request,request.POST)
        if authForm.is_valid():
            user = authForm.get_user()
            login(request,user)
            messages.success(request, 'You are success authenticated')
            return redirect("home_page")
    return render(request,"users/auth.html",{"form":authForm})

def exit(request):
    logout(request)
    messages.success(request, 'You are success exit')
    return redirect("home_page")