from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
# Create your models here.
class Appointment(models.Model):
    name= models.CharField(max_length=25)
    email=models.EmailField()
    title=models.CharField(max_length=25)
    phone = models.IntegerField()
    doctor= models.CharField(max_length=25)
    patient= models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.CharField(max_length=25)
    def __str__(self):
        return self.title
        
        