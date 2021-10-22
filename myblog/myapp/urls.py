from django.urls import path
from . import views


#Create the views
urlpatterns = [
    path('', views.index, name='views'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_new_project', views.add_project, name='add_new_project'),
    path('add_project_step', views.add_project_step, name='add_project_step'),
    path('members', views.members, name='members'),
    path('member_login', views.member_login, name='member_login')
]