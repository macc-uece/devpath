from django.shortcuts import render
from user_manager.forms import UserForm, DevSignUpForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def register(request):
    """docstring"""

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        dev_form = DevSignUpForm(data=request.POST)

        if user_form.is_valid() and dev_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            dev = dev_form.save(commit=False)
            dev.user = user

            if 'profile_picture' in request.FILES:
                dev.profile_picture = request.FILES['profile_picture']

            dev.save()

            registered = True
        else:
            print(user_form.errors, dev_form.errors)
    else:
        user_form = UserForm()
        dev_form = DevSignUpForm()

    return render(
        request,
        'register.html',
        {
            'user_form': user_form,
            'dev_form': dev_form,
            'registered': registered
        }
    )


def dev_login(request):
    """docstring"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard:index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print("Username: {} Password: {}".format(username, password))
            return HttpResponse("invalid credentials")
    else:
        return render(request, "login.html", {})


@login_required
def dev_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard:index'))
