from django.contrib import admin

from resume.models import Bio, Education, Experience, Language, Project, Skill

# Register your models here.

admin.site.register(Bio)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Skill)