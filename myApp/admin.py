"""
This is the configuration file for django admin panel.
"""
from django.contrib import admin
from .models import Details
# Register your models here.
admin.site.register(Details)
