from django.shortcuts import render, redirect
from django.http import response

# Create your views here.
def index(request):
    """
    Creates the homepage
    """
    return render(request, 'index.html')
