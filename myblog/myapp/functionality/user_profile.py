"""This file contains the UserProfile class which represents each user in the project."""

class UserProfile:
    """This class represents each user of the program"""

    def __init__(self, name, contact_email, username) -> None:
        """
        This method initializes a UserProfile object.
        """
        self._name = name
        self._email = contact_email
        self._username = username
        self._projects_involved = list()
    
    def get_name(self):
        """
        Returns the name of the person
        """
        return self._name

    def get_email(self):
        """
        Returns the email address of the person
        """
        return self._email

    def get_username(self):
        """
        Returns the username of the person.
        """
        return self._username

    def get_projects(self):
        """
        Returns a lit with the IDs of all the projects the person is involved in
        """
        return self._projects_involved
    
    def set_name(self, user_name):
        """
        Gets a string and assigns it as the persons name
        """
        self._name = user_name
    
    def set_username(self, new_username):
        """
        Get's a string with the profiles username and assigns it for that profile.
        """
        self._username = new_username
    
    def set_email(self, new_email):
        """
        Get's a string with the email of the profile and assigns it to email.
        """
        self._email = new_email
    
    def add_project(self, project_id):
        """
        Get's a string with the project id and assigns it"""
        self._projects_involved.append(project_id)