import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Registeration

# Create your views here.
def display_views(request):
    s= '<h1>Welcome to Django Classes... first</h1>'
    return HttpResponse(s)

def registration_views(request):
    reg_list=Registeration.objects.all()
    #reg_list=Registeration.objects.filter(name)
    my_dict={'reg_list':reg_list}
    return render(request,'firstapp/wish.html',my_dict)

def datetimeinfo_views(request):
    date=datetime.datetime.now()
    h = int(date.strftime('%H')) #'%H' means 24hours scale using and '%I' means 12hours scales
    msg = '<h1>Welcome Friends,'
    if h<12:
        msg=msg+' Good Morning'
    elif h<16:
        msg=msg+' Good Afternoon'
    elif h<21:
        msg=msg+' Good Evening'
    else:
        msg=msg+' Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'</h1>Now Server time is: '+str(date)+'</h1>'
    return HttpResponse(msg)

def wish_views(request):
    return render(request,'firstapp/wish.html') #render means request html data 

def date_time_views(request):
    date = datetime.datetime.now()
    my_dict = {'msg':date}
    return render(request,'firstapp/datetime.html',context=my_dict) #only my_dict is also valid and direct put {'msg':date} is also valid
    
def info_view(request):
    time = datetime.datetime.now()
    name='Django'
    prerequisite='Python'
    my_dict= {'time':time,'name':name,'prerequisite':prerequisite}
    return render(request,'firstapp/result.html',context=my_dict)

def astro_views(request):
    msg_list=[
        'Very soon, you are going to get marriege!!!',
        'The golden days ahead',
        'Very soon you will get job'
    ]
    name_list=['sunny','Mallika','Katrina','Kareena','Samantha','Priyanka']
    time= datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h<12:
        s='Good Morning'
    elif h<16:
        s='Good Afternoon'
    elif h<21:
        s='Good Evening'
    else:
        s='Good Night'
    name=random.choice(name_list)
    msg=random.choice(msg_list)
    my_dict={'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'firstapp/astrology.html',my_dict)
    
