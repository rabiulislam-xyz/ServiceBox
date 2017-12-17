from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  ListView)

from .models import Service


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

class ServiceUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Service
    fields = ['name','description']
    template_name = 'service/service_create_form.html'

    success_message = 'Service ID: %(id)s Successfully Updated'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id=self.object.id,
        )
