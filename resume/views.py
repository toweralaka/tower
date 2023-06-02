from django.shortcuts import render
from resume.models import Bio, Education, Experience, Language, Project, Skill

# Create your views here.

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'resume/projects.html', context)

def resume(request):
    context = {
        'experiences': Experience.objects.all(),
        'education_list': Education.objects.all(),
        'skill': Skill.objects.all(),
        'languages': Language.objects.all()
    }
    return render(request, 'resume/resume.html', context)
    