from django.shortcuts import render
from .models import Meetings, Profile, ProjectData
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
    meetings = Meetings.objects.all()

    return render(request, 'dashboard.html', {'contents': contents, 'meetings':meetings})

def add_project(request):
    """
    Adds a new project in the database.
    """
    if request.method == 'POST':

        # Collect data from FORM
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        project_owner = request.POST['project_owner']
        deadline = request.POST['project_deadline']
        # Create a ProjectData instance and store the data from the page to the database
        project = ProjectData.objects.create(project_name=project_name, project_description=project_description,
                                             project_owner=project_owner, deadline=deadline)
        project.save()  # Save data in the database

        # Get the latest data from database and load them to the database
        contents = ProjectData.objects.all()
        meetings = Meetings.objects.all()
        return render(request, 'dashboard.html', {'contents':contents, 'meetings':meetings})
    
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
