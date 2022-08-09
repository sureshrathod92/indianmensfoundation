from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display_views(request):
    s= '<h1>Welcome to Django Classes... second</h1>'
    return HttpResponse(s)

def index_views(request):
    return render(request,'firstapp/index.html')
    
def movies_views(request):
    head_msg='Movies Information'
    sub_msg1='RRR ready to release'
    sub_msg2='Background support must be required to get chance'
    sub_msg3='Indian cinema industry struggling like anything with covid'
    sub_msg4='Biggest Benefit of covid for industry: OTT'
    sub_msg5='Suresh is hero of upcoming movies'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5}
    return render(request,'firstapp/news.html',context=my_dict)