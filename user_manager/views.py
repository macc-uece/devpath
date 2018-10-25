from django.shortcuts import render
from user_manager.forms import UserForm, DevSignUpForm


# Create your views here.

def register(request):
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
