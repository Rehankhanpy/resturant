from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
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
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control',  
            'type':'email', 
            })
        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-control',  
            'type':'text', 
            })
        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-control',  
            'type':'text', 
            })
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-control', 
            'name':'password1',   
            'type':'password', 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-control',  
            'type':'password', 
            }) 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
