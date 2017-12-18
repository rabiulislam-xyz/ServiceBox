from django.shortcuts import render
from algoliasearch_django import raw_search

from service.models import Service

def home(request):
    context = {}
    top_service_list = Service.objects.all()

    if request.method == 'POST':
        search_result = raw_search(Service, request.POST.get('q'))
        context["search_result"] = search_result

    context['top_service_list'] = top_service_list
    return render(request, 'website/home.html', context)
