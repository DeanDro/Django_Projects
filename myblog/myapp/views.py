from django.shortcuts import render, redirect
from django.http import response
from .models import ProjectData, Profiles

# Create your views here.
def index(request):
    """
    Creates the homepage
    """
    return render(request, 'index.html')

def login(request):
    """
    Collect login information and confirm authentication
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return render(request, 'dashboard.html', {'username': username, 'password': password})

def dashboard(request):
    """
    Main projects dashboard
    """
    return render(request, 'dashboard.html', {'username': 'Admin'})

def add_project(request):
    """
    Adds a new project in the database.
    """
    return render(request, 'add_new_project.html')

def add_project_step(request):
    """
    Adds a new step in a project.
    """
    return render(request, 'add_project_step.html')

def members(request):
    """
    Returns a list of team members
    """
    return render(request, 'members.html')