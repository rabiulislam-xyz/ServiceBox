from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse

from .forms import UserForm, ProfileForm

@login_required
def dashboard(request):
    context = {
        'user':request.user
    }
    return render(request, 'account/dashboard.html', context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            current_user = User.objects.get(pk=request.user.pk)

            current_user.first_name = user_form.cleaned_data.get('first_name')
            current_user.last_name = user_form.cleaned_data.get('last_name')
            current_user.email = user_form.cleaned_data.get('email')

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