from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
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
            phone = request.POST['phone'],
            permission = int(request.POST['permission']),
        )
        profile.save()
        return HttpResponse("회원가입 완료")        
    else:
        return render(request, 'signup.html')
        

def login(request):
    return render(request, 'login.html')