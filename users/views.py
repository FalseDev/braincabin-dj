from django.shortcuts import render, redirect
from django.contrib import messages
from django_email_verification import sendConfirm
from django.views.generic import ListView, DetailView
from .models import User, Profile
from . import forms


def profile_edit(request):
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
            profile = request.user.profile
            profile.status = form.cleaned_data['status']
            profile.institute = form.cleaned_data['institute']
            profile.save()
            messages.success(request, 'Profile updated!')
            return redirect('user-detail', pk=request.user.pk)
    else:
        form = forms.UserProfileForm()
    return render(request, 'users/update-profile.html', {"form":form})


class UserListView(ListView):
    model = User
    paginate_by = 18
    ordering = 'username'


class UserDetailView(DetailView):
    model = User


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            sendConfirm(user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for user {username}!')
            return redirect('confirm-mail-message')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {"form":form})

def confirm_mail(request):
    return render(request, 'users/confirm-mail-message.html')