from django.shortcuts import render, redirect
from django.http import response

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