from django.shortcuts import render, redirect
from user_manager.models import User, Developer
from dev_resume.models import Skill, Education, Project, Experience


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'index.html')

def add_skill(request):
    if request.method == 'POST':
        user_name = request.user.get_username()
        user = User.objects.get(username=user_name)
        dev = Developer.objects.get(user=user)
        
        return render(request, 'skills.html')
    elif request.method == 'GET':
        skills = Skill.objects.all()
        return render(request, 'skills.html', context={'skills': skills})
    else:
        return render(request, 'skills.html')

def add_education(request):
    if request.method == 'POST':
        user_name = request.user.get_username()
        user = User.objects.get(username=user_name)
        dev = Developer.objects.get(user=user)
        
        return render(request, 'education.html')
    elif request.method == 'GET':
        eds = Education.objects.all()
        return render(request, 'education.html', context={'eds': eds})
    else:
        return render(request, 'education.html')

def add_experience(request):
    if request.method == 'POST':
        user_name = request.user.get_username()
        user = User.objects.get(username=user_name)
        dev = Developer.objects.get(user=user)
        
        return render(request, 'experiences.html')
    elif request.method == 'GET':
        exps = Experience.objects.all()
        return render(request, 'experiences.html', context={'exps': exps})
    else:
        return render(request, 'experiences.html')

def add_project(request):
    if request.method == 'POST':
        user_name = request.user.get_username()
        user = User.objects.get(username=user_name)
        dev = Developer.objects.get(user=user)
        
        return render(request, 'projects.html')
    elif request.method == 'GET':
        projects = Project.objects.all()
        return render(request, 'projects.html', context={'projects': projects})
    else:
        return render(request, 'projects.html')

def load_resume(request):
        return render(request, 'all.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')

# def list_skills(request):
#     skills = Skill.objects.all()
#     return render(request,'skills.html',{'skills':skills})

# def create_skill(request):
#     form = SkillForm(request.POST or None)
#     if form.is_valid() :
#         form.save()
#         return redirect('list_skills')

#     return render(request, 'skill-form.html',{'form':form})

# def update_skill(request, id):
#     skill = Skill.objects.get(id = id)
#     form = SkillForm(request.POST or None, instance = skill)

#     if form.is_valid():
#         form.save()
#         return redirect('list_skills')

#     return render(request, 'skill-form.html',{'form':form, 'skill': skill})

# def delete_skill(request, id):
#     skill = Skill.objects.get(id = id)

#     if request.method == 'POST':
#         skill.delete()
#         return redirect('list_skills')

#     return render(request, 'skill-delete-confirm.html', {'skill': skill})