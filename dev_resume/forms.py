from django import forms
from dev_resume.models import Resume, Skill


# Your forms go here

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('skills', 'studies', 'experiences', 'projects')
