from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50,help_text="Emter a valid email address")

    class Meta:
        model = Account
        fields = ('email','username','password1','password2')

class Userauth(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email,password= password):
            raise forms.ValidationError(" Enter Valid login details!! ")

