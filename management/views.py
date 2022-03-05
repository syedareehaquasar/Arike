from email.policy import default
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .forms import MyUserCreationForm
from management.models import MyUser

class UserCreateView(CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = "user/signup.html"
