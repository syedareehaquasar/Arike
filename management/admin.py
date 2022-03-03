from django.contrib import admin

from management.models import User

admin.sites.site.register(User)
