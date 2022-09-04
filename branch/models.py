from email.policy import default
from pyexpat import model
from django.db import models

class data(models.Model):
    Id=models.IntegerField(default=0, null='true')
    Name=models.CharField(max_length=30)
    Userid=models.CharField(max_length=30)
    Password=models.IntegerField(default=0)
