from django.db import models

# Create your models here.
class Registeration(models.Model):
    cno= models.IntegerField()
    cname = models.CharField(max_length=60)
    cmob = models.BigIntegerField()
    cmail = models.EmailField()
    caddr = models.TextField()
    csal = models.FloatField()
    cdob=models.DateField()
    cmarks= models.IntegerField()

#after creating models before runserver makemigrations is compulsory