from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=60) 
    
    class meta:
        model = User
        fieilds = ('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True):
        user = super(signupform,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
            