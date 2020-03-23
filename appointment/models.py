from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Appointment(models.Model):
    email=models.EmailField(max_length=254,default="none@example.com")
    title=models.CharField(max_length=25)
    phone = models.IntegerField()
    doctor= models.CharField(max_length=25, default="none")
    patient= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.CharField(max_length=25)
    timer=models.CharField(max_length=25)
    def __str__(self):
        return self.title
        
        