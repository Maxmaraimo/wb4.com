import logging
from math import e

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, UserForm, UserUpdateForm
from .usecases import *

log = logging.getLogger(__name__)


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        p_form = ProfileForm(request.POST,
                             instance=request.user.profile,
                             files=request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=True)
            profile = p_form.save(commit=True)
            messages.success(request,
                             f"Your account has been updated!")
            return redirect('profile')
        else:
            context = {
                "u_form": u_form,
                "p_form": p_form,
            }
            return render(request, 'profile.html', context)

    context = {
        'u_form': UserUpdateForm(instance=request.user),
        'p_form': ProfileForm(instance=request.user.profile)
    }
    return render(request, 'profile.html', context)

# 


def wb4pay(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/wb4pay.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/wb4pay.html', context)



def video(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/video.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/video.html', context)

def support(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/support.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/support.html', context)

def stickers(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/stickers.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/stickers.html', context)

def services(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/services.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/services.html', context)

def photos(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/photos.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/photos.html', context)

def news(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/news.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/news.html', context)

def music(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/music.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/music.html', context)

def message(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/message.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/message.html', context)

def markett(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/markett.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/markett.html', context)

def groups(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/groups.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/groups.html', context)

def game(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/game.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/game.html', context)

def clips(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/clips.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/clips.html', context)

def calls(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/calls.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/calls.html', context)

def friends(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'templatesField/friends.html', context)

    context = {'form': UserForm()}
    return render(request, 'templatesField/friends.html', context)

