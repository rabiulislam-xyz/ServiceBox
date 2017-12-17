from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class ServiceManager(models.Manager):
    def my_service_list(self, id):
        return self.filter(provider__id=id)


class Service(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField()

    provider        = models.ForeignKey(User, on_delete=models.CASCADE)

    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects         = ServiceManager()

    def get_absolute_url(self):
        return reverse('service:service_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name