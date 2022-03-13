"""arike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("user/create/", UserCreateView.as_view()),

    path("login/", UserLoginView.as_view()),
    path("logout/", LogoutView.as_view()),

    path("facility/", FacilityListView.as_view()),
    path("facility/create/", FacilityCreateView.as_view()),
    path("facility/update/<pk>/", FacilityUpdateView.as_view()),
    path("facility/delete/<pk>/", FacilityDeleteView.as_view()),
    path("facility/detail/<pk>/", FacilityDetailView.as_view()),

    path("patient/", PatientListView.as_view()),
    path("patient/create/", PatientCreateView.as_view()),
    path("patient/update/<pk>/", PatientUpdateView.as_view()),
    path("patient/delete/<pk>/", PatientDeleteView.as_view()),

    path("treatment/", TreatmentListView.as_view()),
    path("treatment/create/", TreatmentCreateView.as_view()),
    path("treatment/update/<pk>/", TreatmentUpdateView.as_view()),
    path("treatment/delete/<pk>/", TreatmentDeleteView.as_view()),

    path("family/", FamilyListView.as_view()),
    path("family/create/", FamilyCreateView.as_view()),
    path("family/update/<pk>/", FamilyUpdateView.as_view()),
    path("family/delete/<pk>/", FamilyDeleteView.as_view()),

    path("disease/", DiseaseListView.as_view()),
    path("disease/create/", DiseaseCreateView.as_view()),
    path("disease/update/<pk>/", DiseaseUpdateView.as_view()),
    path("disease/delete/<pk>/", DiseaseDeleteView.as_view()),

    path("visit/", VisitListView.as_view()),
     path("visit/details/create/", VisitDetailsCreateView.as_view()),
     path("visit/details/<pk>/", VisitDetailsListView.as_view()),
    path("visit/create/", VisitCreateView.as_view()),
    path("visit/update/<pk>/", VisitUpdateView.as_view()),
    path("visit/delete/<pk>/", VisitDeleteView.as_view()),
    
    path("dashboard/", Dashboard.as_view()),
    path("", UserLoginView.as_view()),
]
