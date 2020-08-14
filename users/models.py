from django.db import models

# Create your models here.

class Data(models.Model):
    first=models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email=models.EmailField()
    gender=models.CharField(max_length=100,)