from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .register_login_form import UserLoginForm,CustomUserCreationForm



# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid Input')

       
    else:
        registration_form = CustomUserCreationForm()
    
    context = {'form':registration_form}
    return render(request, 'user/register.html', context)

def userLogin(request):
    
    login_form = UserLoginForm()
    context = {'form':login_form}
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist!') 

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User successfully logged in!")
            return redirect('url')
        else:
            messages.error(request, 'username or password is not valid!!!')
    return render(request, 'user/login.html', context)


def userLogout(request):
    logout(request)
    print("User successfully logged out!")
    return redirect('login')
