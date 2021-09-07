from django.db import models
from .functionality.user_profile import UserProfile
from .functionality.projects import Project, ProjectStep

# Create your models here.
class ProjectData(models.Model):

    """This class contains the data for each project"""
    project_name = models.CharField(max_length=40, default='New Meeting')


class Profiles(models.Model):

    """This class represents a user in the database"""

    profile_name = models.CharField(max_length=40, default='admin')
