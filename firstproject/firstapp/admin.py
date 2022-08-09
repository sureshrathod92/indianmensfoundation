from django.contrib import admin
from firstapp.models import Registeration
# Register your models here.
class Registerationadmin(admin.ModelAdmin):
    list_display= ['cno','cname','cmob','cmail','caddr','csal','cmarks','cdob']

admin.site.register(Registeration,Registerationadmin)