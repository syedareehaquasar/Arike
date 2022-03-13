from django.contrib import admin

from .models import *

admin.sites.site.register(UserProfile)
admin.sites.site.register(Ward)
admin.sites.site.register(lsg_body)
admin.sites.site.register(District)
admin.sites.site.register(Facility)
admin.sites.site.register(Patient)
admin.sites.site.register(State)
admin.sites.site.register(Family_Detail)
admin.sites.site.register(Patient_Disease)
admin.sites.site.register(Treatment)
admin.sites.site.register(Disease)
