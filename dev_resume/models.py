from django.db import models


# Create your models here.

class Resume(models.Model):
    pass


class Skill(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    skill_type = models.ForeignKey(
        to='SkillType',
        on_delete=models.SET_NULL,
        related_name='type',
        null=False,
        blank=False
    )
    # level = models.PositiveSmallIntegerField()


class SkillType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)


class Project(models.Model):
    pass


class ProjectType(models.Model):
    pass


class Education(models.Model):
    pass


class EducationType(models.Model):
    pass


class Experience(models.Model):
    pass


class ExperienceType(models.Model):
    pass
