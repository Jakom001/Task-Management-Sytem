from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'address']
    ordering = ['id']


admin.site.register(Profile, ProfileAdmin)
