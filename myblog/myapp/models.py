from django.db import models
from .functionality.user_profile import UserProfile
from .functionality.projects import Project, ProjectStep

# Create your models here.
class ProjectData(models.Model):

    """This class contains the data for each project"""
    name = models.CharField(max_length=100, default='Next meeting')
    description = models.CharField(max_length=200, default='Setup next meeting')
    owner = models.CharField(max_length=50, default='secretary')
    members = models.CharField(max_length=500, default='Team')
    start_date = models.DateField(default=('2021', '9', '6'))
    deadline = models.DateField(default=('2021', '9', '15'))


class Profiles(models.Model):

    """This class represents a user in the database"""

    name = models.CharField(max_length=50, default='admin')
    email = models.CharField(max_length=200, default='random@random.com')
    username = models.CharField(max_length=40, default='admin')
