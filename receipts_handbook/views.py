from django.shortcuts import render
from .models import TeamMember, Recipt
from .forms import ReciptForm
from django.shortcuts import redirect
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

def rec_new(request):
    if request.method == "POST":
        form = ReciptForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return render(request,'receipts_handbook/receipts.html',{})
    else:
        form = ReciptForm()
    return render(request, 'receipts_handbook/rec_edit.html', {'form': form})

    
def dev_contacts(request):
    members=TeamMember.objects.all()
    return render(request,'receipts_handbook/dev_contacts.html',{'members':members})
# Create your views here.
