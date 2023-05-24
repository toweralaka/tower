from django.shortcuts import render
from resume.models import Bio, Experience, Project

# Create your views here.

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'resume/projects.html', context)

def resume(request):
    context = {
        'experiences': Experience.objects.all(),
        'bio': Bio.objects.all()
    }
    return render(request, 'resume/resume.html', context)
    