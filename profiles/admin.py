from django.contrib import admin
from .models import UserProfile, Profile

# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('id', 'name', 'level',)
    list_filter = ('name',)

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ('fkuser', 'fkprofile',)
    list_filter = ('fkprofile',)