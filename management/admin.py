from django.contrib import admin

from management.models import MyUser

admin.sites.site.register(MyUser)
