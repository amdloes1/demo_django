from django.db import models

# Create your models here.
class my_user( models.Model):
    name = models.CharField(max_length= 30)
    age = models.IntegerField()
    city =models.CharField(max_length= 30)
