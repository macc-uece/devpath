from django.contrib import admin
from dev_resume.models import (
    Resume,
    Experience, Education, Skill, Project,
    ProjectType, SkillType, EducationType, ExperienceType
)

# Register your models here.

admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(SkillType)
admin.site.register(ProjectType)
admin.site.register(EducationType)
admin.site.register(ExperienceType)
