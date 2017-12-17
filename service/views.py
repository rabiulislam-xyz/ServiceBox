from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView)

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Service
from .forms import ServiceModelForm


class ServiceDetail(DetailView):
    model = Service
    template_name = 'service/service_detail.html'

class ServiceList(ListView):
    model = Service
    template_name = 'service/service_list.html'

class MyServiceList(ListView):
    def get_queryset(self):
        Service.objects.my_service_list(self.request.user.id)
    template_name = 'service/service_list.html'

class ServiceCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Service
    fields = ['name','description']
    template_name = 'service/service_create_form.html'

    # default CreateView not creating 'User ForeignKey' on Create Form
    # thus it not adding service.provider field to current user
    # so we have to add it manually!
    def form_valid(self, form):
        form.instance.provider = self.request.user
        return super(ServiceCreate, self).form_valid(form)

    success_message = 'Service ID: %(id)s Successfully Created'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )

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





