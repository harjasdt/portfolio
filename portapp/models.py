from django.db import models

# Create your models here.
class QUESTION(models.Model):
    temp=models.FloatField(default=-1,blank=False)
    ph=models.FloatField(default=-1,blank=False)
    mos=models.FloatField(default=-1,blank=False)
    n=models.FloatField(default=-1,blank=False)
    p=models.FloatField(default=-1,blank=False)
    k=models.FloatField(default=-1,blank=False)
    time=models.CharField(max_length=100,blank=False,default=9)

    # def __str__(self):
    #     return self.temp

class HISTORY(models.Model):
    crop=models.CharField(max_length=100)
    time=models.CharField(max_length=100,blank=False,default=9)

class DOOR(models.Model):
    d1=models.IntegerField(default=-1,blank=False)
    d2=models.IntegerField(default=-1,blank=False)
    time=models.CharField(max_length=100,blank=False,default=9)

class DOORFAIL(models.Model):
    d1=models.IntegerField(default=-1,blank=False)
    d2=models.IntegerField(default=-1,blank=False)
    time=models.CharField(max_length=100,blank=False,default=9)
    

class ACTIVE(models.Model):
    active=models.IntegerField(default=0,blank=False)
    activatetime=models.CharField(max_length=100,blank=False,default=9)
    

class TEMP(models.Model):
    temp=models.CharField(max_length=100,blank=False,default=9)
    activatetime=models.CharField(max_length=100,blank=False,default=9)