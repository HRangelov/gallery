from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from accounts.forms import SignUpForm, UserProfileForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'paintings': user.userprofile.painting_set.all(),
            'form': UserProfileForm(),
        }

        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


# def signup_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': SignUpForm(),
#         }
#
#         return render(request, 'accounts/signup.html', context)
#     else:
#         # Dxe5yct3WeHcCfVbVYzaf4T3W70Aainx
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             profile = UserProfile(
#                 user=user,
#             )
#             profile.save()
#
#             login(request, user)
#             return redirect('current user profile')
#
#         context = {
#             'form': form,
#         }
#
#         return render(request, 'accounts/signup.html', context)

class RegisterView(TemplateView):
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = SignUpForm()
        context['profile_form'] = UserProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # @receiver is used for signals

            # profile = profile_form.save(commit=False)
            # profile.user = user
            # profile.save()

            login(request, user)
            return redirect('current user profile')

        context = {
            'user_form': SignUpForm(),
            'profile_form': UserProfileForm(),
        }

        return render(request, 'accounts/signup.html', context)


# def signout_user(request):
#     logout(request)
#     return redirect('index')

class SignOutView(LogoutView):
    next_page = reverse_lazy('index')