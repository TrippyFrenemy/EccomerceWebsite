from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from shop.models import Orders


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text="youremail@gmail.com")


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2", "email")


class OrderForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    telephone = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=50, required=True)

