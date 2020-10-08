from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST['id'],
            password = request.POST['password'],
            email = request.POST['email']
        )
        profile = Profile(
            user = user,
            name = request.POST['name'],
            nickname = request.POST['nickname'],
            phone = request.POST['phone'],
            permission = int(request.POST['permission']),
        )
        profile.save()
        return render(request, 'complete_signup.html', { 'signup_user':user})       
    else:
        return render(request, 'signup.html')
        

def login(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',
            {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')