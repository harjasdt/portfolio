from django.db import models

# Create your models here.
class QUESTION(models.Model):
    temp=models.TextField(max_length=300,blank=False)
    time=models.IntegerField(blank=False,default=9)
