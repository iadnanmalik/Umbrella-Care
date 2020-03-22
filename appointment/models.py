from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
# Create your models here.
class Appointment(models.Model):
    title=models.CharField(max_length=25)
    phone = models.IntegerField()
    patient= models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField()
    def __str__(self):
        return self.title
        
        