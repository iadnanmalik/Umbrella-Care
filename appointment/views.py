from django.shortcuts import render,redirect
from .models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'appointment/home.html')
@login_required(redirect_field_name='login')
def makeappointment(request):
    if request.method=='POST':          
        if request.user.is_staff==True:
            return redirect('login')
        else:
            if request.POST['doctor']  and request.POST['phone'] and request.POST['date']:
                appointment=Appointment()
                appointment.title=request.POST['title']
                appointment.patient=request.user
                appointment.phone=request.POST['phone']
                appointment.date=request.POST['date']
                appointment.save()
                return redirect('home')
            else:
                return render(request,'appointment/appointments.html', {'error':'Please Fill all the information'})
            
    else:


        return render(request, 'appointment/appointments.html')
