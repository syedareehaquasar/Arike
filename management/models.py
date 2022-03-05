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

    def __str__(self):
        return self.user.username