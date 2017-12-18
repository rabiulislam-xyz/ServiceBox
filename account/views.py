from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse

from .forms import UserForm, ProfileForm
from service.models import Service


@login_required
def dashboard(request):
    # show all services for current user
    user_service_list = Service.objects.my_service_list(request.user.id)
    context = {
        'user':request.user,
        'user_service_list': user_service_list,
    }
    return render(request, 'account/dashboard.html', context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # get current user and add updated info to
            # User and its Profile model
            current_user = User.objects.get(pk=request.user.pk)

            # adding info to User model
            current_user.first_name = user_form.cleaned_data.get('first_name')
            current_user.last_name = user_form.cleaned_data.get('last_name')
            current_user.email = user_form.cleaned_data.get('email')

            # adding info to user's Profile model
            current_user.profile.photo = profile_form.cleaned_data.get('photo')
            current_user.profile.website = profile_form.cleaned_data.get('website')
            current_user.profile.location = profile_form.cleaned_data.get('location')

            current_user.save()
            return redirect(reverse('account:dashboard'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'account/profile_update_form.html', context)