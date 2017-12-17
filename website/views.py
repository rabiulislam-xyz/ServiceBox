from django.shortcuts import render

from service.models import Service

def home(request):
    top_service_list = Service.objects.all()

    context = {
        'top_service_list': top_service_list,
    }
    return render(request, 'website/home.html', context)
