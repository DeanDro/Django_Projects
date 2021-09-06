from django.db import models
from .functionality.user_profile import UserProfile
from .functionality.projects import Project, ProjectStep

# Create your models here.
class ProjectData(models.Model):

    """This class contains the data for each project"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.CharField(max_length=50)
    members = models.CharField(max_length=500)
    start_date = models.DateField()
    deadline = models.DateField()


class Profiles(models.Model):

    """This class represents a user in the database"""

    def __init__(self, name, email, username) -> None:
        """
        Initializes the profile in the database.
        """
        self._new_user = UserProfile(name, email, username)