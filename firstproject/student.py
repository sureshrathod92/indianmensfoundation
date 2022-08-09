import os

from Django.firstproject.firstapp.models import Registeration
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

from faker import Faker
from random import *
fakegen= Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        froll =fakegen.random_int(min=1,max=999)
        fname=fakegen.name()
        fdob= fakegen.date()
        fmarks=fakegen.random_int(min=1,max=100)
        femail=fakegen.cmail()
        fno=phonenumbergen()
        faddr=fakegen.address()
        student_record=Registeration.objects.get_or_create(rollno=froll,name=fname,dob=fdob,marks=fmarks,email=femail,fno=fno,caddr=faddr)
    populate(20)
