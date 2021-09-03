from django.urls import path
from . import views


#Create the views
urlpatterns = [
    path('', views.index, name='views'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]