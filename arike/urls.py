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
from django.urls import path
from django.contrib.auth.views import LogoutView

from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", UserCreateView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("dashboard/", Dashboard.as_view()),
    path("user/logout/", LogoutView.as_view()),

    path('facility/add/', facilityCreationView.as_view()),
    path("facility/", ListFacilities.as_view()),
    path("facility/update/<pk>/", facilityUpdateView.as_view()),
    path("facility/delete/<pk>/", facilityDeleteView.as_view()),

    path("patient/add/", addPatientView.as_view()),
    path("patient/update/<pk>/", patientUpdateView.as_view()),
    path("patient/", ListPatients.as_view()),
    path("patient/delete/<pk>/", patientDeleteView.as_view()),

    path("family/add/", addFamilyDetails.as_view()),
    path("family/", addFamilyDetails.as_view()),
    path("family/delete/<pk>/", familyDeleteView.as_view()),

    path("treatment/add/", addTreatmentDetails.as_view()),
    path("treatment/", addTreatmentDetails.as_view()),
    path("treatment/delete/<pk>/", treatmentDeleteView.as_view()),
    
    path("", UserLoginView.as_view()),
]
