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

class UserCreateForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailInput()
    phone = forms.CharField(max_length=14)
    is_verified = forms.BooleanField()
    role = forms.ChoiceField(choices=TYPES_OF_USERS)
    password = forms.PasswordInput()

    class Meta:
        model = User

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        return user

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "./user/signup.html"