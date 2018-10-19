from django.shortcuts import render
from django.contrib.auth.models import (
    User
)
from django.contrib.auth.forms import (
    UserCreationForm,
)

from django.urls import (
    reverse_lazy,
)

from django.views.generic import (
    CreateView,
)


# Create your views here.

class RegisterView(CreateView):
    # model = User
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard:list_skills')