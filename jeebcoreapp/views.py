from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jeebcoreapp.forms import UserForm, CoreForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User # user submit data
# Create your views here.
def home(request):
    return redirect(core_home)

@login_required(login_url='/core/sign-in/')
def core_home(request):
    return render(request, 'core/home.html', {})


def core_sign_up(request):
    user_form = UserForm()
    core_form = CoreForm()

    # check method POST ?
    if request.method == "POST":
        user_form = UserForm(request.POST)
        core_form = CoreForm(request.POST, request.FILES) # request.FILES คืออะไร!!!!!

        # check data is valid?
        if user_form.is_valid() and core_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_core = core_form.save(commit=False)
            new_core.user = new_user
            new_core.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(core_home)


    return render(request, 'core/sign_up.html', {
        "user_form": user_form,
        "core_form": core_form
    })
