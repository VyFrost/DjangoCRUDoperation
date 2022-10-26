from contextlib import nullcontext
from email.policy import default
from django.db import models

# Create your models here.
class personal_data(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField(default='null')
    pin=models.IntegerField()
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name + "'s" + " "+'data'