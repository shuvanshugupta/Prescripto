from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from .models import Profile
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('start')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        doct = int(request.POST['doctor'])
        if doct == 1:
            doct = True
        descr = request.POST['descr']
        if password1==password2:
            if Profile.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = Profile.objects.create_user( username=username,password=password1 ,email=email, first_name=first_name, last_name=last_name, contact=contact, descr=descr, doctor= doct)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('index')
    else:
        return render(request,"re.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,"login.html")