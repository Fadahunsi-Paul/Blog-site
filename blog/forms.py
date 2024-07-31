from django import forms
from blog.models.profile import Profile
from account.models import User

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    username= forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    class Meta:
        model =User
        fields=['username','email']

class ProfileForm(forms.ModelForm):    
    image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Profile
        fields = ['image']