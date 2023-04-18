from django.db import models

class table(models.Model):
    
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    Email = models.EmailField(max_length=100)
    Phone_number = models.IntegerField(blank=False)
    Password = models.CharField(max_length=500)

    def __str__(self):
        return self.Firstname


    

class business(models.Model):
    business_name = models.CharField(max_length=30)
    contact_number = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    streetaddress2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    postalcode = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)

    def __str__(self):
        return self.business_name
