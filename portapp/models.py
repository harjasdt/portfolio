from django.db import models

# Create your models here.
class QUESTION(models.Model):
    q1=models.IntegerField(blank=False,default=9)
    q2=models.IntegerField(blank=False,default=9)
