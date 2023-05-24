from django.db import models

# Create your models here.
class QUESTION(models.Model):
    temp=models.DecimalField(blank=False,decimal_places=2,max_digits=8,default=0)
    time=models.IntegerField(blank=False,default=9)
