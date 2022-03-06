from django.contrib import admin

from .models import MyUser

admin.sites.site.register(MyUser)
