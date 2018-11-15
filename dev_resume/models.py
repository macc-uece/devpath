from django.db import models
# from user_manager.models import Developer


# Create your models here.

class Resume(models.Model):
    last_update = models.DateTimeField()

    owner = models.ForeignKey(
        to='user_manager.Developer',
        on_delete=models.DO_NOTHING,
        related_name='dev_id',
        null=False,
        blank=False
    )

    skills = models.ManyToManyField(
        to='Skill',
        through='ResumeSkill',
        related_name='dev_skills',
        blank=True
    )

    projects = models.ManyToManyField(
        to='Project',
        related_name='dev_projects',
        blank=True
    )

    studies = models.ManyToManyField(
        to='Education',
        through='ResumeEducation',
        related_name='dev_education',
        blank=True
    )

    experiences = models.ManyToManyField(
        to='Experience',
        through='ResumeExperience',
        related_name='dev_experience',
        blank=True
    )


class Skill(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    skill_type = models.ForeignKey(
        to='SkillType',
        on_delete=models.SET_NULL,
        related_name='skill_type',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class SkillType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class ResumeSkill(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.DO_NOTHING)
    skill = models.ForeignKey('Skill', on_delete=models.DO_NOTHING)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{} {} {}".format(self.resume_id, self.skill_id, self.level)

    class Meta:
        unique_together = ('resume',
                           'skill',
                           'level')


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    project_type = models.ForeignKey(
        to='ProjectType',
        on_delete=models.SET_NULL,
        related_name='project_type',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    education_type = models.ForeignKey(
        to='EducationType',
        on_delete=models.SET_NULL,
        related_name='education_type',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class EducationType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ResumeEducation(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.DO_NOTHING)
    education = models.ForeignKey('Education', on_delete=models.DO_NOTHING)
    level = models.PositiveSmallIntegerField()
    start = models.DateTimeField(null=False, blank=False)
    finish = models.DateTimeField()

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.resume_id, self.education_id,
            self.level, self.start, self.finish)

    class Meta:
        unique_together = ('resume',
                           'education',
                           'level')


class Experience(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    experience_type = models.ForeignKey(
        to='EducationType',
        on_delete=models.SET_NULL,
        related_name='experience_type',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ExperienceType(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ResumeExperience(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.DO_NOTHING)
    experience = models.ForeignKey('Experience', on_delete=models.DO_NOTHING)
    level = models.PositiveSmallIntegerField()
    start = models.DateTimeField(null=False, blank=False)
    finish = models.DateTimeField()

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.resume_id, self.experience_id,
            self.level, self.start, self.finish)

    class Meta:
        unique_together = ('resume',
                           'experience',
                           'level')
