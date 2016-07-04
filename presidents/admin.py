from django.contrib import admin
from .models import President
# Register your models here.

@admin.register(President)
class AdminPresident(admin.ModelAdmin):
	list_display = ('id', 'full_name', 'position')
	list_filter = ('id',)