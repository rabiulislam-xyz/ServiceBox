from django import forms

from .models import Service


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['provider']  # provider will be add in view, for security.
