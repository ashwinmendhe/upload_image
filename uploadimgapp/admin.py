from django.contrib import admin
from . models import profile
# Register your models here.

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'picture']