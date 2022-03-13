from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["is_verified"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["role"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["facility"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["district"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["user"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta:
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district", "user")


class UserProfileForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
            
    class Meta:
        model = UserProfile
        fields = ("password", "phone", "is_verified", "role", "facility", "district")
        
class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district", "deleted")

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["password"].widget.attrs[
            "class"
        ] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"


class FacilityCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"

    class Meta(forms.ModelForm):
        model = Facility
        fields = ("kind", "name", "address", "pincode", "phone", "ward", "deleted")

class AddPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"

    class Meta(forms.ModelForm):
        model = Patient
        fields = ("full_name", "date_of_birth", "address", "landmark", "phone", "gender", "emergency_phone_number", "ward", "facility", "deleted")

class AddFamilyDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted" and field != "is_primary":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"
    class Meta(forms.ModelForm):
        model = Family_Detail
        fields = ("full_name", "date_of_birth", "phone", "email", "relation", "address", "education", "occupation", "remarks", "is_primary", "patient", "deleted")

class addTreatment(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"
    class Meta(forms.ModelForm):
        model = Treatment
        fields = ("description", "care_type", "care_sub_type", "patient", "nurse", "deleted")

class addPatientDisease(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"
    class Meta(forms.ModelForm):
        model = Patient_Disease
        fields = ("patient", "disease", "treatment", "note", "nurse", "deleted")

class addDisease(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Disease
        fields = ("name", "icds_code")


class scheduleVisit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != "deleted":
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
            else:
                self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 my-4 bg-gray-200/75 rounded-lg"
    class Meta(forms.ModelForm):
        model = Schedule_Visit
        fields = ("date", "time", "duration", "patient", "nurse", "deleted")

class addVisitDetails(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Visit_Details
        fields = ("palliative_phase", "blood_pressure", "pulse", "general_random_blood_sugar", "personal_hygiene", "mouth_hygiene", "pubic_hygiene", "systemic_examination", "patient_at_peace", "pain", "symptoms", "note", "visit_schedule")

class addWard(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Ward
        fields = ("name", "number", "lsg")
    
class addLSG(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = lsg_body
        fields = ("name", "kind", "lsg_body_code", "district")


class addDistrict(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = District
        fields = ("name", "state")


class addState(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 dark:text-purple-900 text-purple-900 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = State
        fields = ("name",)