from django.shortcuts import render,redirect
from .models import Appointment
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'appointment/home.html')
@login_required(redirect_field_name='login')
def makeappointment(request):
    if request.user.is_staff==True:
        return render(request,'appointment/viewappointment.html')
        

    else:
            
        if request.method=='POST':          
            if request.POST['doctor']  and request.POST['phone'] and request.POST['date']:
                appointment=Appointment()
                appointment.title=request.POST['title']
                appointment.patient=request.user
                appointment.phone=request.POST['phone']
                appointment.date=request.POST['date']
                appointment.timer=request.POST['timer']
                appointment.email=request.POST['email']
                appointment.doctor=request.POST['doctor']
                appointment.save()
                subject='Appointment Confirmation'
                Premessage='Your Appointment has been confirmed with  Title '
                message=Premessage + appointment.title + ' DAY :' + appointment.date + ' TIME : ' + appointment.timer + ' at Doctor ' + appointment.doctor 
                from_email=settings.EMAIL_HOST_USER
                to_list=[appointment.email,settings.EMAIL_HOST_USER]
                send_mail(subject,message,from_email,to_list,fail_silently=True)
                return render(request,'appointment/details.html',{
                    'name':appointment.patient,
                    'phone':appointment.phone,
                    'doctor':appointment.doctor,
                    'email':appointment.email,
                    'date':appointment.date,
                    'time':appointment.timer               
                })

            else:
                return render(request,'appointment/appointments.html', {'error':'Please Fill all the information'})
            
        else:


            return render(request, 'appointment/appointments.html')
def viewappointment(request):
    if request.method=='POST':
        appointments=Appointment.objects          
        docname=request.POST['doctor']
        return render(request,'appointment/detailappointment.html',{'docname':docname,'appointments':appointments})
            
    else:
        return redirect('home')
    
