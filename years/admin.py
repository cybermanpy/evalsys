from django.contrib import admin
from .models import Year
# Register your models here.

@admin.register(Year)
class AdminYear(admin.ModelAdmin):
    list_display = ('id', 'description', 'date',)
    list_filter = ('date',)