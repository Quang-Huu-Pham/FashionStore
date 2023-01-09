from django.contrib import admin
from .models import ProfileUser
# Register your models here.


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'phone']


admin.site.register(ProfileUser, AdminProfile)
