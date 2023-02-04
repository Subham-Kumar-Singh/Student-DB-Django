from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    roll = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
