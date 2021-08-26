from django.db import models

# Create your models here.

class Admin(models.Model):
    Username = models.CharField(max_length=100,default="xyz@12")
    Upassword = models.CharField(max_length=255,default="password")