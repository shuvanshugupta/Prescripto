from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
import smtplib
from .models import appointment
from customuser.models import Profile
from django.contrib import messages
import time
import datetime as dt
import threading
import urllib.request
import urllib.parse
from django.contrib.auth import get_user_model
 
timelist = {}

# Create your views here.

def appointlist(request):
    if request.user.doctor == True:
        appoints2 = get_list_or_404(appointment,dkey=request.user.pk)
        appoints = appoints2
    else:
        appoints1 = get_list_or_404(appointment,pkey=request.user.pk)
        appoints = appoints1
    return render(request,'past.html',{'appoints': appoints})

def start(request):
    threadObj = threading.Thread(target=emails)
    threadObj.start()
    return render(request,'start.html')

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"ab.html")

def appoint(request):
    User = get_user_model()
    if request.method == 'POST':
        a = appointment()
        a.pkey = request.user.pk
        dname = request.POST['dname']
        print(dname)
        dobj = get_object_or_404(User, first_name=dname)
        a.dkey = dobj.pk
        a.content = request.POST['descr']
        a.date = request.POST['date']
        a.stime = request.POST['stime']
        a.etime = request.POST['etime']
        mail_top =  get_object_or_404(User, pk= a.pkey)
        mail_tod =  get_object_or_404(User, pk= a.dkey)
        a.save()
        appobj = get_object_or_404(appointment,etime=a.etime,date=a.date)
        akey = appobj.pk
        timelist[akey]= a.date +" "+ a.etime + ":00"
        send_email(mail_top.email,a)
        print("Email sent to patient")
        send_email(mail_tod.email,a)
        print("Email sent to doctor")
        return redirect('index')
    else:
        doctors = list()
        doctors = User.objects.filter(doctor= True)
        return render(request,"app.html",{'doctors':doctors})

def send_email(send_to,ta):
    email_user = 'app.prescripto@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'psqpnizekjrbamuw')

    #EMAIL
    message = 'Here is a new appointment either by you or to you if uou are doctor\nDate:'+ str(ta.date)+'\nTime'+str(ta.stime)+'to'+str(ta.etime)+'\nDescription:'+str(ta.content) +'\nPrescripto - By Team Gryffindor'
    server.sendmail(email_user, send_to , message)
    server.quit()

def send_email_at(send_time,send_to,ta):
    time.sleep(send_time.timestamp() - time.time())
    send_email(send_to,ta)
    print('email sent')
    #msg = 'Have you forgot this task\nTask: '+ str(ta.content)+'\nToDo- A Reminder Web Application'
    #resp =  sendSMS('c49igJPDn1Q-URH8PBcuvPcpP6Pk2Cj5ixxkpSvPf8', '91'+str(u.contact),msg)
    #print (resp)
    #print('message sent')
    ta.passed= True

def emails():
    User = get_user_model()
    for it in sorted(timelist):
        send_time = dt.datetime.strptime(timelist[it],"%Y-%m-%d %H:%M:%S")
        ta = get_object_or_404(appointment,pk= it)
        pobj = get_object_or_404(User,pk=ta.pkey)
        dobj = get_object_or_404(User,pk=ta.dkey)
        send_to = pobj.email
        send_email_at(send_time,send_to,ta)
        send_to = dobj.email
        send_email_at(send_time,send_to,ta)
        timelist.pop(it)
        