from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('main_info',views.main_info,name='main_info'),
    path('team_members/',views.team_members,name='team_members'),
    path('dev_contacts/',views.dev_contacts,name='dev_contacts'),
]