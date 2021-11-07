from django.shortcuts import render
from .models import TeamMember, Recipt

def index(request):
    return render(request,'receipts_handbook/index.html',{})

def profile(request):
    return render(request,'receipts_handbook/profile.html',{})

def receipts(request):
    return render(request,'receipts_handbook/receipts.html',{})

def main_info(request):
    return render(request,'receipts_handbook/main_info.html',{})

def team_members(request):
    members=TeamMember.objects.all()
    return render(request,'receipts_handbook/team_members.html',{'members':members})

def dev_contacts(request):
    members=TeamMember.objects.all()
    return render(request,'receipts_handbook/dev_contacts.html',{'members':members})
# Create your views here.
