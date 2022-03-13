from datetime import date
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from management.forms import *
from management.models import *


class UserCreateView(CreateView):
    model = UserProfile
    form_class = MyUserCreationForm
    template_name = "user/signup.html"
    success_url = "/login/"


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "user/login.html"
    success_url = "/dashboard/"


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"


class UserUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user/update.html"
    success_url = "/dashboard"


class FacilityListView(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "facility/list.html"
    context_object_name = "facility"
    paginate_by = 5

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)


class FacilityCreateView(CreateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/add.html"
    success_url = "/facility/"


class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = "delete.html"
    success_url = "/facility/"


class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facility/detail.html"


class FacilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/update.html"
    success_url = "/dashboard/"


class PatientListView(ListView):
    queryset = Patient.objects.filter(deleted=False)
    template_name = "patient/list.html"
    context_object_name = "patient"
    paginate_by = 5

    def get_queryset(self):
        return Patient.objects.filter(deleted=False)


class PatientCreateView(CreateView):
    model = Patient
    form_class = AddPatientForm
    template_name = "patient/add.html"
    success_url = "/patient"


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "delete.html"
    success_url = "/patient"


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = AddPatientForm
    template_name = "patient/update.html"
    success_url = "/patient"


class TreatmentListView(ListView):
    queryset = Treatment.objects.filter(deleted=False)
    template_name = "patient/treatment.html"
    context_object_name = "treatment"
    paginate_by = 5

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Treatment.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = addTreatment
    template_name = "patient/addTreatment.html"
    success_url = "/treatment"


class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = "delete.html"
    success_url = "/treatment"


class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = addTreatment
    template_name = "patient/treatmentUpdate.html"
    success_url = "/treatment"


class FamilyListView(ListView):
    queryset = Family_Detail.objects.filter(deleted=False)
    template_name = "patient/FamilyList.html"
    context_object_name = "family"
    paginate_by = 5

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Family_Detail.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class FamilyCreateView(CreateView):
    model = Family_Detail
    form_class = AddFamilyDetailsForm
    template_name = "patient/addFamilyDetails.html"
    success_url = "/family"


class FamilyDeleteView(DeleteView):
    model = Family_Detail
    template_name = "delete.html"
    success_url = "/family"


class FamilyUpdateView(UpdateView):
    model = Family_Detail
    form_class = AddFamilyDetailsForm
    template_name = "patient/familyUpdate.html"
    success_url = "/family"


class DiseaseListView(ListView):
    queryset = Patient_Disease.objects.filter(deleted=False)
    template_name = "disease/list.html"
    context_object_name = "disease"
    paginate_by = 5

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Patient_Disease.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class DiseaseCreateView(CreateView):
    model = Patient_Disease
    form_class = addDisease
    template_name = "disease/create.html"
    success_url = "/disease"


class DiseaseDeleteView(DeleteView):
    model = Patient_Disease
    template_name = "delete.html"
    success_url = "/disease"


class DiseaseUpdateView(UpdateView):
    model = Schedule_Visit
    form_class = addDisease
    template_name = "disease/update.html"
    success_url = "/disease"


class VisitListView(ListView):
    queryset = Schedule_Visit.objects.filter(deleted=False)
    template_name = "visits/list.html"
    context_object_name = "visit"
    paginate_by = 5

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Schedule_Visit.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class VisitCreateView(CreateView):
    model = Schedule_Visit
    form_class = scheduleVisit
    template_name = "visits/create.html"
    success_url = "/visit"

class VisitDetailsListView(DetailView):
    model = Visit_Details
    template_name = "visits/detail.html"

class VisitDetailsCreateView(CreateView):
    model = Visit_Details
    form_class = addVisitDetails
    template_name = "visits/create.html"
    success_url = "/visit"


class VisitDeleteView(DeleteView):
    model = Schedule_Visit
    template_name = "delete.html"
    success_url = "/visit"


class VisitUpdateView(UpdateView):
    model = Schedule_Visit
    form_class = scheduleVisit
    template_name = "visits/update.html"
    success_url = "/visit"
