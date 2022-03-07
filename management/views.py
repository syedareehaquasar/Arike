from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView

from .forms import MyUserCreationForm, CustomAuthenticationForm
from management.models import UserProfile

class UserCreateView(CreateView):
    model = UserProfile
    form_class = MyUserCreationForm
    template_name = "user/signup.html"
    success_url = "/login"
class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "user/login.html"

# forms for each (4)
# update view later

class Dashboard(TemplateView):
    template_name = "dashboard.html"


class facilityCreationView(CreateView):
    pass

class addPatientView(CreateView):
    pass

class addFamilyDetails(CreateView):
    pass

class addPatientDisease(CreateView):
    pass
