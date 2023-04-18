from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.username



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0) #cents

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)