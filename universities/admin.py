from django.contrib import admin
from .models import University
# Register your models here.

@admin.register(University)
class AdminUniversity(admin.ModelAdmin):
	list_display = ('id', 'name', 'direction', 'postal_code',)
	list_filter = ('name',)

# @admin.register(HaveDepartment)
# class AdminHaveDepartment(admin.ModelAdmin):
# 	list_display = ('dep', 'uni',)
# 	list_filter = ('dep', 'uni',)