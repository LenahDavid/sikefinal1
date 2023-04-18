from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import table,business
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from rest_framework import viewsets
from .serializer import TableSerializers
from django.core.mail import send_mail
# import math,random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')                   
        Password = request.POST.get('password')

        user = auth,authenticate(request,Email=Email, Password=Password)

        if user is not None:
            messages.success(request, f' wecome {Email} !!')
            return redirect('about-us.html')
        else:
            error_message =  'Invalid login credentials'
            return render(request, 'login.html', {'error_message': error_message})
      #   else:
      #       messages.info(request,'invalid credentials')
      #       return redirect('signup.html')
    else:
        return render(request, 'login.html')

def signup(request):
     if request.method == 'POST':
         Firstname = request.POST['first-name']
         Lastname = request.POST['last-name']
         surname = request.POST['surname']
         Email = request.POST['email']
         Phone_number = request.POST['phone-number']
         Age = request.POST['age']
         Gender = request.POST['gender']
         nationality = request.POST['nationality']
         City = request.POST['city']
         country = request.POST['country']
         address1 = request.POST['address1']
         Address2 = request.POST['address2']
         PostalCode = request.POST['postal-code']
         Password = request.POST['create-password']
         confirmPassword = request.POST['confirm-password']

         if Password == confirmPassword:
            if table.objects.filter(Email=Email).exists():
                messages.info(request,'Email already used')
                return redirect('signup.html')

            elif table.objects.filter(Phone_number=Phone_number).exists():
                messages.info(request,'phonenumber already exists')
                return redirect('signup.html')
            else:
                user=table.objects.create(Firstname=Firstname, Lastname=Lastname, surname=surname, Email=Email,Phone_number=Phone_number,Age=Age, Gender=Gender,nationality=nationality, City=City,country=country,address1=address1,Address2=Address2,PostalCode=PostalCode,Password=Password)
                user.save()
                return redirect('dashboard.html')
         else:
            messages.info(request,'password is not the same')
            return redirect('signup.html')
     else:
        return render(request, 'signup.html')
def aboutus(request):
    return render(request, 'about-us.html')

def businessregform(request):
    if request.method == 'POST':
         business_name = request.POST['business name']
         contact_number = request.POST['contact number']
         email = request.POST['email']
         country = request.POST['Country']
         street_address = request.POST['Street Address']
         streetaddress2 = request.POST['Street address 2']
         city = request.POST['city']
         region = request.POST['Region']
         postalcode = request.POST['Postal/Zip code']
         password = request.POST['password']
         confirmpassword = request.POST['confirm password']

         if password == confirmpassword:
            if business.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('businessregform.html')
            elif business.objects.filter(contact_number=contact_number).exists():
                messages.info(request,'phonenumber already exists')
                return redirect('businessregform.html')
            else:
                user=business.objects.create(business_name=business_name, contact_number=contact_number, email=email, region=region,postalcode=postalcode, city=city,country=country,street_address=street_address,streetaddress2=streetaddress2,password=password)
                user.save()
                return redirect('dashboard.html')
         else:
            messages.info(request,'password is not the same')
            return redirect('businessregform.html')
    else:
        return render(request, 'businessregform.html')


def logout(request):
    authenticate.logout(request)
    return redirect('about-us.html')

def dashboard(request):
    return render(request, 'dashboard.html')
