from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import table

from django.contrib import messages
from django.contrib.auth import authenticate,login




# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if pass1!=pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
#         else:

#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')


def signup(request):
     if request.method == 'POST':
         Firstname = request.POST.get('first-name')
         Lastname = request.POST.get('last-name')
         surname = request.POST.get('surname')
         Email = request.POST.get('email')
         Phone_number = request.POST.get('phone-number')
         Password = request.POST.get('create-password')
         confirmPassword = request.POST.get('confirm-password')

         if Password == confirmPassword:
            if table.objects.filter(Email=Email).exists():
                messages.info(request,'Email already used')
                return render(request,'signup.html')

            elif table.objects.filter(Phone_number=Phone_number).exists():
                messages.info(request,'phonenumber already exists')
                return render(request, 'signup.html')
            else:
                user=table.objects.create(Firstname=Firstname, Lastname=Lastname, surname=surname, Email=Email,Phone_number=Phone_number,Password=Password)
                user.save()
                return redirect('login/')
         else:
            messages.info(request,'password is not the same')
            return render(request,'signup.html')
     else:
        return render(request, 'signup.html')
# def aboutus(request):
#     return render(request, 'about-us.html')

# def businessregform(request):
#     if request.method == 'POST':
#          business_name = request.POST['business name']
#          contact_number = request.POST['contact number']
#          email = request.POST['email']
#          country = request.POST['Country']
#          street_address = request.POST['Street Address']
#          streetaddress2 = request.POST['Street address 2']
#          city = request.POST['city']

#          postalcode = request.POST['Postal/Zip code']
#          password = request.POST['password']
#          confirmpassword = request.POST['confirm password']

#          if password == confirmpassword:
#             if business.objects.filter(email=email).exists():
#                 messages.info(request,'Email already used')
#                 return redirect('businessregform.html')
#             elif business.objects.filter(contact_number=contact_number).exists():
#                 messages.info(request,'phonenumber already exists')
#                 return redirect('businessregform.html')
#             else:
#                 user=business.objects.create(business_name=business_name, contact_number=contact_number, email=email, region=region,postalcode=postalcode, city=city,country=country,street_address=street_address,streetaddress2=streetaddress2,password=password)
#                 user.save()
#                 return redirect('dashboard.html')
#          else:
#             messages.info(request,'password is not the same')
#             return redirect('businessregform.html')
#     else:
#         return render(request, 'businessregform.html')

        





def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('app')  # Redirect to home page
        else:
            # messages.error(request, 'Invalid email or password.')
            return HttpResponse ("invalid credentials")
    
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def app(request):
  return render(request,'app.html')