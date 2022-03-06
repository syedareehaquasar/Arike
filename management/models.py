from django.db import models

from django.contrib.auth.models import AbstractUser

TYPES_OF_USERS = (
    ("primary_nurse", "primary_nurse"),
    ("secondary_nurse", "secondary_nurse"),
    ("district_admin", "district_admin")
)

class MyUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, choices=TYPES_OF_USERS, default=TYPES_OF_USERS[0][0])
    phone = models.CharField(max_length=14)
    is_verified = models.BooleanField("Is Verified?", default=False)
        
DISTRICT_CHOICES = [
    (1, "Thiruvananthapuram"),
    (2, "Kollam"),
    (3, "Pathanamthitta"),
    (4, "Alappuzha"),
    (5, "Kottayam"),
    (6, "Idukki"),
    (7, "Ernakulam"),
    (8, "Thrissur"),
    (9, "Palakkad"),
    (10, "Malappuram"),
    (11, "Kozhikode"),
    (12, "Wayanad"),
    (13, "Kannur"),
    (14, "Kasargode"),
]


class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


LOCAL_BODY_CHOICES = (
    # Panchayath levels
    (1, "Grama Panchayath"),
    (2, "Block Panchayath"),
    (3, "District Panchayath"),
    (4, "Nagar Panchayath"),
    # Municipality levels
    (10, "Municipality"),
    # Corporation levels
    (20, "Corporation"),
    # Unknown
    (50, "Others"),
)

def reverse_lower_choices(choices):
    output = {}
    for choice in choices:
        output[choice[1].lower()] = choice[0]
    return output


REVERSE_LOCAL_BODY_CHOICES = reverse_lower_choices(LOCAL_BODY_CHOICES)


class LocalBody(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    body_type = models.IntegerField(choices=LOCAL_BODY_CHOICES)
    localbody_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = (
            "district",
            "body_type",
            "name",
        )

    def __str__(self):
        return f"{self.name} ({self.body_type})"


class Ward(models.Model):
    local_body = models.ForeignKey(LocalBody, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    user = models.ManyToManyField(MyUser)

    def __str__(self):
        return f"{self.name}"


PHCorCHC = (
    ("PHC", "PHC"),
    ("CHC", "CHC")
)
class Facility(models.Model):
    kind = models.CharField(max_length=100, choices=PHCorCHC, default=TYPES_OF_USERS[0][0])
    name = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=15)
    phone = models.CharField(max_length=14)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    user = models.ManyToManyField(MyUser)

class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.TextField()
    landmark = models.CharField(max_length=15)
    phone = models.CharField(max_length=14)
    gender = models.CharField(max_length=15)
    emergency_phone_number = models.CharField(max_length=14)
    expired_time = models.DateTimeField(default=None)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT)

RELATIONS = (
    ("Mother", "Mother"),
    ("Father", "Father"),
    ("Sibling", "Sibling"),
    ("Spouse", "Spouse"),
    ("Guardian", "Guardian"),
    ("Friend", "Friend"),
    ("Grand Parents", "Grand Parents"),
    ("Not Related", "Not Related"),
)
class FamilyDetails(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    dob = models.DateField()
    email = models.EmailField()
    relation = models.CharField(max_length=100, choices=RELATIONS, default=TYPES_OF_USERS[0][0])
    address = models.TextField()
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

DISEASES = (
    ("DM", "D-32"),
    ("Hypertension", "HT-58"),
    ("IHD", "IDH-21"),
    ("COPD", "DPOC-144"),
    ("Dementia", "DM-62"),
    ("CVA", "CAV-89"),
    ("Cancer", "C-98"),
    ("CKD", "DC-25"),
)
class Disease(models.Model):
    disease = models.CharField(max_length=100, choices=DISEASES, default=TYPES_OF_USERS[0][0])

class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    disease = models.ForeignKey(Disease, on_delete=models.PROTECT)
    note = models.TextField()

class VisitSchedule:
    pass

class VisitDetails:
    pass

class Treatment:
    pass

class TreatmentNotes:
    pass

