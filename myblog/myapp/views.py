from django.shortcuts import render
from django.http import response

# Create your views here.
def index(request):
    """
    Creates the homepage
    """
    return response.HttpResponse('<h1>Welcome</h1>')
