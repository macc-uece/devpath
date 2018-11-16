from django import forms
from django.contrib.auth.models import User
from user_manager.models import Developer


# Create your forms here

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # username = forms.TextInput(attrs={'class': 'form-control'})
    # email = forms.TextInput(attrs={'class': 'form-control'})
    # password = forms.TextInput(attrs={'class': 'form-control'})
    # first_name = forms.TextInput(attrs={'class': 'form-control'})
    # last_name = forms.TextInput(attrs={'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class DevSignUpForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('profile_picture', )