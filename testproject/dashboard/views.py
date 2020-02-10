from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from testapp.models import CustomUser, CustomUserManager

# Create your views here.
def dashboard(request):

    return render(request, 'bbvoy/index.html', {})

def dash(request):
    return render(request, 'bbvoy/account.html')

def create_user(request):
    
    if request.method == "POST":
        user = User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
        user.save()

        user = authenticate(request.POST['email'], request.POST['password'])
        return redirect('/dashboard')
    else:
        return render(request, 'bbvoy/register.html', {})
    
    return HttpResponse()

def sign_in(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
        
    else:
        # Return an 'invalid login' error message.
        return ('email or password information invalid')