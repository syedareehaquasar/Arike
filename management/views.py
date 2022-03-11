from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect

from .forms import *
from management.models import *

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
    success_url = "/facility/"

class facilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "update.html"
    success_url = "/facility/"

class facilityDeleteView(DeleteView):
    model = Facility
    template_name = "delete.html"
    success_url = "/facility/"

class ListFacilities(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "facility/list.html"
    context_object_name = "facility"
    paginate_by = 10

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)


class addPatientView(CreateView):
    model = Patient
    form_class = AddPatientForm
    template_name = "patient/add.html"
    success_url = "/patient/"

class patientUpdateView(UpdateView):
    model = Patient
    form_class = AddPatientForm
    template_name = "update.html"
    success_url = "/patient/"

class patientDeleteView(DeleteView):
    model = Patient
    template_name = "delete.html"
    success_url = "/patient/"

class ListPatients(ListView):
    queryset = Patient.objects.filter(deleted=False)
    template_name = "patient/list.html"
    context_object_name = "patient"
    paginate_by = 10

    def get_queryset(self):
        return Patient.objects.filter(deleted=False)

class addFamilyDetails(CreateView):
    model = Family_Detail
    form_class = AddFamilyDetailsForm
    template_name = "patient/addfamilyDetails.html"
    success_url = "/dashboard"

class familyUpdateView(UpdateView):
    model = Family_Detail
    form_class = AddFamilyDetailsForm
    template_name = "update.html"
    success_url = "/dashboard/"

class familyDeleteView(DeleteView):
    model = Family_Detail
    template_name = "delete.html"
    success_url = "/dashboard/"

class addTreatmentDetails(CreateView):
    model = Treatment
    form_class = addTreatment
    template_name = "patient/addTreatment.html"
    success_url = "/dashboard"

class treatmentUpdateView(UpdateView):
    model = Treatment
    form_class = addTreatment
    template_name = "update.html"
    success_url = "/dashboard/"

class treatmentDeleteView(DeleteView):
    model = Treatment
    template_name = "delete.html"
    success_url = "/dashboard/"