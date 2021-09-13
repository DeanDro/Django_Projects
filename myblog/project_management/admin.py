from django.contrib import admin
from .models import ProjectData, Profile, Meetings

# Register your models here.
admin.site.register(ProjectData)
admin.site.register(Profile)
admin.site.register(Meetings)