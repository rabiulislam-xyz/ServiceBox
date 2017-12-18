from django.db.models import Q
from django.shortcuts import render
from algoliasearch_django import raw_search

from service.models import Service
from .forms import SearchForm

def home(request):
    context = {}
    top_service_list = Service.objects.all()

    context['top_service_list'] = top_service_list
    return render(request, 'website/home.html', context)


def search(request):
    context = {}
    print(request.GET)
    q = request.GET.get('q')
    if q:
        # setting custom search result
        results = Service.objects.filter(Q(name__icontains=q)|
                                         Q(description__icontains=q)|
                                         Q(provider__first_name__contains=q)|
                                         Q(provider__last_name__contains=q)).distinct()
        context['results']= results

        # adding algolia search result
        algolia_results = raw_search(Service, q)
        context["algolia_results"] = algolia_results

    form = SearchForm(request.GET or None)
    context['form']=form
    return render(request, 'website/search_result.html', context)
