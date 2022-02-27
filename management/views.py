from email.policy import default
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django import forms
from management.models import User

TYPES_OF_USERS = (
    ("primary_nurse", "primary_nurse"),
    ("secondary_nurse", "secondary_nurse"),
    ("district_admin", "district_admin")
)

class CustomUserForm(forms.ModelForm):
    # full_name = forms.CharField(max_length=100)
    # email = forms.EmailInput()
    # phone = forms.CharField(max_length=14)
    # is_verified = forms.BooleanField()
    # role = forms.ChoiceField(choices=TYPES_OF_USERS)
    # password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["full_name", "email", "phone", "is_verified", "role"]

class UserCreateView(CreateView):
    form_class = CustomUserForm
    template_name = "./user/signup.html"