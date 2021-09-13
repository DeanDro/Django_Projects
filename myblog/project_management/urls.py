from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
     path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_new_project', views.add_project, name='add_new_project'),
    path('add_project_step', views.add_project_step, name='add_project_step'),
    path('members', views.members, name='members'),
    path('projects_list', views.projects_list, name='projects_list'),
    path('meetings', views.meetings_list, name='meetings_list')
]


