from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField, DateTimeField

# Create your models here.

class ProjectData(models.Model):
    """This class represents a project"""

    project_name = models.CharField(max_length=100, default='Next Meeting')
    project_owner = models.CharField(max_length=100, default='K')
    project_description = models.CharField(max_length=150, default='Setup the team meeting for next week')
    members_list = models.CharField(max_length=150, default='myself')
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    deadline = models.CharField(max_length=12)
    project_completed = models.CharField(max_length=10, default='No')


class Profile(models.Model):
    """This class represents the profile of a user"""

    username = models.CharField(max_length=50, default='admin_user')
    name = models.CharField(max_length=50, default='admin')
    email = models.CharField(max_length=40, default='admin@admin_mail.com')
    position = models.CharField(max_length=50, default='member')