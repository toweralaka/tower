from django.urls import path, include
from django.views.generic.base import TemplateView
from resume.views import resume, projects

# app_name = 'resume'

urlpatterns = [
    path('', TemplateView.as_view(template_name='base/index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='resume/about.html'), name='about'),
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),
]
