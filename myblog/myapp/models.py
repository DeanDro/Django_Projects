from django.db import models
from .functionality.user_profile import UserProfile
from .functionality.projects import Project, ProjectStep

# Create your models here.
class ProjectData:

    """This class contains the data for each project"""

    def __init__(self, name, description, owner, deadline) -> None:
        new_project = Project(name, description, owner, deadline)


class Profiles:

    """This class represents a user in the database"""

    def __init__(self, name, email, username) -> None:
        new_user = UserProfile(name, email, username)