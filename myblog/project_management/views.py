from django.shortcuts import render
from .models import Meetings, Profile, ProjectData
from .functionality.dashboard_view import Status, confirm_meeting
import datetime

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
    all_meetings = Meetings.objects.all()   # Get all meetings
    today_date = datetime.datetime.now()
     # Get current date
    current_day = today_date.date().today()
    # Get upcoming meetings
    meetings = confirm_meeting(all_meetings, today_date)

    # Collect data from form
    if request.method == 'POST':
        meeting_name = request.POST['Name']
        meeting_description = request.POST['Description']
        meeting_date = request.POST['Date']
        meeting_agenda = request.POST['Agenda']

        # Register form into database
        meeting_registration = Meetings.objects.create(meeting_name=meeting_name, date=meeting_date, 
                                                       description=meeting_description, agenda=meeting_agenda)
        meeting_registration.save()

    return render(request, 'meetings.html', {'meetings':meetings, 'today':current_day})
