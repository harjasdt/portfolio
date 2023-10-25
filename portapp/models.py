from django.db import models

# Create your models here.
class QUESTION(models.Model):
    temp=models.CharField(max_length=900)
    time=models.IntegerField(blank=False,default=9)
