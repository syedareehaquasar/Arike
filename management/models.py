from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        abstract = True
class State(TimeStampMixin):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
class District(TimeStampMixin):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
class lsg_body(TimeStampMixin):
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
    name = models.CharField(max_length=255)
    kind = models.IntegerField(choices=LOCAL_BODY_CHOICES)
    lsg_body_code = models.CharField(max_length=20, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.kind})"
class Ward(TimeStampMixin):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=30)
    lsg = models.ForeignKey(lsg_body, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
class Facility(TimeStampMixin):
    FACILITY_CHOICES = (
        ("PHC", "PHC"),
        ("CHC", "CHC"),
    )
    kind = models.CharField(max_length=100, choices=FACILITY_CHOICES)
    name = models.CharField(max_length=255)
    address = models.TextField()
    pincode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
class UserProfile(TimeStampMixin):
    ROLE_CHOICES = (
        ("primary_nurse", "primary_nurse"),
        ("secondary_nurse", "secondary_nurse"),
        ("district_admin", "district_admin"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True)
    
    USERNAME_FIELD = 'user.username'

    def __str__(self):
        return f"{self.user.username}"
        
class Patient(TimeStampMixin):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    landmark = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    emergency_phone_number = models.CharField(max_length=30)
    expired_time = models.DateTimeField(blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.full_name}"
class Family_Detail(TimeStampMixin):
    RELATION_CHOICES = (
        ("MOTHER", "MOTHER"),
        ("FATHER", "FATHER"),
        ("SON", "SON"),
        ("DAUGHTER", "DAUGHTER"),
        ("BROTHER", "BROTHER"),
        ("SISTER", "SISTER"),
        ("WIFE", "WIFE"),
        ("HUSBAND", "HUSBAND"),
        ("OTHER", "OTHER")
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254)
    relation = models.CharField(max_length=100, choices=RELATION_CHOICES)
    address = models.TextField()
    education = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.full_name}"
class Disease(TimeStampMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    icds_code = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"
class Treatment(TimeStampMixin):
    CARETYPE_CHOICES = (
        ("General_care", "General_care"),
        ("Genito_urinary_care", "Genito_urinary_care")
    )
    description = models.TextField()
    care_type = models.CharField(max_length=255, choices=CARETYPE_CHOICES)
    care_sub_type = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, blank=True, null=True)
    nurse = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.care_type}"
class Patient_Disease(TimeStampMixin):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, blank=True, null=True)
    disease = models.ForeignKey(
        Disease, on_delete=models.CASCADE, blank=True, null=True)
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField()
    nurse = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.disease}"
class Schedule_Visit(TimeStampMixin):
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, blank=True, null=True)
    nurse = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    deleted = models.BooleanField(default=False)
class Visit_Details(TimeStampMixin):
    YESORNO_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO")
    )
    palliative_phase = models.CharField(max_length=255)
    blood_pressure = models.CharField(max_length=255)
    pulse = models.CharField(max_length=255)
    general_random_blood_sugar = models.CharField(max_length=255)
    personal_hygiene = models.CharField(max_length=255)
    mouth_hygiene = models.CharField(max_length=255)
    pubic_hygiene = models.CharField(max_length=255)
    systemic_examination = models.CharField(max_length=255)
    patient_at_peace = models.CharField(
        max_length=255, choices=YESORNO_CHOICES)
    pain = models.CharField(max_length=255, choices=YESORNO_CHOICES)
    symptoms = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    visit_schedule = models.ForeignKey(
        Schedule_Visit, on_delete=models.CASCADE, null=True, blank=True)