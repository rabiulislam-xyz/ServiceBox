from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Service
from .forms import ServiceModelForm


def service_detial(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {
        'service': service
    }
    return render(request, 'service/service_detail.html', context)


def service_list(request):
    print(request)
    all_services = Service.objects.all()
    context = {
        'service_list': all_services
    }
    return render(request, 'service/service_list.html', context)


def my_service_list(request):
    my_services = Service.objects.my_service_list(request.user.id)
    context = {
        'service_list': my_services
    }
    return render(request, 'service/service_list.html', context)


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            # ServiceModelForm not creating 'User ForeignKey'
            # thus it not adding service.provider field to current user
            # so we have to add it manually!
            form.instance.provider = request.user
            form.save()
            # redirect user to newly created service detail page
            return redirect(form.instance)
    else:
        form = ServiceModelForm()
    return render(request, 'service/service_create_form.html', {'form': form})


@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)

    # checking if the current user is creator of
    # this service, only creators can update theirs services
    if not service.provider.id == request.user.id:
        raise Http404

    if request.method == 'POST':
        form = ServiceModelForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect(service)
    else:
        form = ServiceModelForm(instance=service)
    return render(request, 'service/service_create_form.html', {'form': form})
