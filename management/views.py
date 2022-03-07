from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView

from .forms import MyUserCreationForm, CustomAuthenticationForm, FacilityCreationForm
from management.models import Facility, UserProfile

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

class Pannel(TemplateView):
    template_name = "pannel.html"

class facilityCreationView(CreateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/add.html"
    success_url = "/dashboard/"

class ListFacilities(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "facility/list.html"
    context_object_name = "facility"
    paginate_by = 10

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)


class addPatientView(CreateView):
    pass

class addFamilyDetails(CreateView):
    pass

class addPatientDisease(CreateView):
    pass
