from django.contrib import admin
from .models import ProjectData, Profiles

# Register your models here.
admin.site.register(Profiles)
admin.site.register(ProjectData)