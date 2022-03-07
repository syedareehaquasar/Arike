from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district")


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district")

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["password"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"


class FacilityCreationForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Facility
        fields = ("kind", "name", "address", "pincode", "phone", "ward", "deleted")

class AddPatientForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Patient
        fields = ("full_name", "date_of_birth", "address", "landmark", "phone", "gender", "emergency_phone_number", "expired_time", "ward", "facility", "deleted")

# class AddFamilyDetailsForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = UserProfile
#         fields = ("phone", "email", "is_verified", "role", "facility", "ward")

# class addPatientDisease(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = UserProfile
#         fields = ("phone", "email", "is_verified", "role", "facility", "ward")