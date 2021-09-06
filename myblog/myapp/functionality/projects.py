"""This file holds the Projects and ProjectStep classes that represent a project and each step of a project
respectively."""

import datetime
import random


class ProjectStep:
    """This class represents each project step in an overall project"""

    def __init__(self, name, owner) -> None:
        """
        It initializes a project step.
        """
        self._name = name
        self._owner = owner
        self._description = name
        self._nextStep = None
    
    def get_name(self):
        """
        Returns the name of the project.
        """
        return self._name

    def get_owner(self):
        """
        Returns this step's owner
        """
        return self._owner

    def get_description(self):
        """
        Returns description of this step.
        """
        return self._description
    
    def get_nextStep(self):
        """
        Returns the next step in the project. If it is none then you are in the
        final step of the project.
        """
        return self._nextStep

    def set_owner(self, new_owner):
        """
        Sets the owner of the step
        """
        self._owner = new_owner

    def set_name(self, new_name):
        """
        Sets the name of the step.
        """
        self._name = new_name

    def set_nextStep(self, new_nextStep):
        """
        Sets what is the next step.
        """
        self._nextStep = new_nextStep

    def set_description(self, new_description):
        """
        Sets the description for this project.
        """
        self._description = new_description


class Project:

    """This class represents a project"""

    def __init__(self, name, description, owner, deadline) -> None:
        """
        Initializes a project. deadline must be given as a tuple with yyyy, mm, dd
        """
        self._id = str(random.random()) + name
        self._name = name
        self._description = description
        self._owner = owner
        self._members_list = list()
        self._start_date = datetime.datetime.now()
        self._deadline = datetime.datetime(deadline)
        self._head = None
        self._next_step = None

    def get_name(self):
        """
        Returns the name of the project
        """
        return self._name

    def get_description(self):
        """
        Returns the project description
        """
        return self._description

    def get_owner(self):
        """
        Returns project owner
        """
        return self._owner

    def get_members(self):
        """
        Returns a list with the members of the project
        """
        return self._members_list

    def get_starting_date(self):
        """
        Returns the date the project started.
        """
        return self._start_date
    
    def get_deadline(self):
        """
        Returns the deadline date for this project.
        """
        return self._deadline
    
    def get_head(self):
        """
        Returns the head of the linked list of steps for this project. This is an
        instance of ProjectStep object.
        """
        return self._head

    def get_next_step(self):
        """
        Returns the next step in the linked list. This will be an instance of ProjectStep.
        """
        return self._next_step

    def set_owner(self, new_owner):
        """
        You set a new owner for the project.
        """
        self._owner = new_owner

    def set_name(self, new_name):
        """
        Sets a new name for the project owner.
        """
        self._name = new_name

    def set_description(self, new_description):
        """
        Sets a new description for the project.
        """
        self._description = new_description
    
    def set_members(self, new_members):
        """
        Takes a list of UserProfile objects and assigns them in the members list.
        """
        self._members_list = new_members
    
    def add_member(self, new_member):
        """
        Takes as a parameter a UserProfile and adds in the list of members for this project.
        """
        self._members_list.append(new_member)
    
    def set_deadline(self, new_deadline):
        """
        Gets as a parameter a tuple of numbers in the form (yyyy, mm, dd) and sets it as the new
        deadline date for the project.
        """
        self._deadline = new_deadline
    
    def set_head(self, new_ProjectStep):
        """
        Takes as a parameter an instace of ProjectStep object and assigns it as the head of the project.
        """
        self._head = new_ProjectStep
    
    def set_next_step(self, next_projectStep):
        """
        Takes as a parameter a projectStep instance object and assigns it as the next node in the linked
        list of projects. 
        """
        self._next_step = next_projectStep

    def add_next_step(self, step_name, step_owner):
        """Creates a step and adds it in the linked list of steps"""
        new_step = ProjectStep(step_name, step_owner)
        if self._head is None:
            self._head = new_step
        else:
            current_node = self._head
            while current_node.get_nextStep() is not None:
                current_node = current_node.get_nextStep()
            current_node.set_nextStep(new_step)
        new_step.set_nextStep(None)
