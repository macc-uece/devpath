from django.shortcuts import render, redirect
from .models import Skill
from .forms import SkillForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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