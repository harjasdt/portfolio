from django.db import models

# Create your models here.
class QUESTION(models.Model):
    temp=models.FloatField(default=-1,blank=False)
    ph=models.FloatField(default=-1,blank=False)
    mos=models.FloatField(default=-1,blank=False)
    n=models.FloatField(default=-1,blank=False)
    p=models.FloatField(default=-1,blank=False)
    k=models.FloatField(default=-1,blank=False)
    time=models.IntegerField(blank=False,default=9)

    # def __str__(self):
    #     return self.temp
