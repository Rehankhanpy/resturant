from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import account

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    phone_number = forms.CharField(max_length=40)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-control',
            'name':'username',  
            'type':'text', 
            'maxlength': '16', 
            'minlength': '6', 
            'placeholder':'Enter Your Username',
            }) 
        self.fields['phone_number'].widget.attrs.update({
            'class':'form-control',
            'type':'text',
            'name':'phone_number',
            'placeholder':'Enter Your Phone Number',
        })
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'email', 
            'type':'email', 
            'placeholder':'Enter Your Email Address',
            })
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'password1',   
            'type':'password', 
            'placeholder':'Enter Password',
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-control',  
            'name':'password2',
            'type':'password', 
            'placeholder':'Confirm Password',
            }) 
    class Meta:
        model = account
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
    
