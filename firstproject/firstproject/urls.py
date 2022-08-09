"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from firstapp import views
#from firstapp import views as v1 #if u have multiple application then u must define alias name
#from secondapp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello1/', v1.display),
    #path('datetime/',views.datetimeinfo_views),
    #path('hello2/', v2.display),
    path('firstapp/',include('firstapp.urls')),
    path('secondapp/',include('secondapp.urls')),
]
