from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html',{
        "username": request.user.username,
        "password": request.user.password
    })

def user_login(request):
    return render (request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse("user_auth:login")

        )
    else:
        login(request,user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


# Create your views here.
