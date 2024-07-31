from django import forms
from django.contrib.auth import get_user_model
from blog.models.profile import Profile
from account.models import User

User = get_user_model

class RegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Username'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Email Address',
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Enter Password',
                'minlenght':'8',
    
            }
        )
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Re-Enter Password',
                'minlenght':'8',
                
            }
        )
    )   

    class Meta:
        model=User
        fields =['email']

class LoginForm(forms.Form):
    email= forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Enter Email',
                
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Enter Password',
                'minlenght':8
            }
        )
    )

class UserUpdateForm(forms.Form):
    email= forms.EmailField()

    class Meta:
        model =  User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']