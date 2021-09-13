from django.shortcuts import render
from .models import Profile, ProjectData
from .functionality.dashboard_view import Status

# Create your views here.

def index(request):
    """
    The purpose of this app is to return the login page
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
    contents = ProjectData.objects.all()
    status = Status(contents)

    return render(request, 'dashboard.html', {'contents': contents})

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
    profiles = Profile.objects.all()
    return render(request, 'members.html', {'profiles': profiles})

def projects_list(request):
    """
    Returns a list of all projects
    """
    projects = ProjectData.objects.all()
    return render(request, 'projects_list.html', {projects: projects})

def meetings_list(request):
    """
    Returns a page with all upcoming meetings and past meetings
    """
    return render(request, 'meetings.html')
