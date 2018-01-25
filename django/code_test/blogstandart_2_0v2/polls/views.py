from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from .models import Catalog
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.contrib.auth.models import User
#from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def index(request):
    #catalog_list = Catalog.objects.all()


    catalog_list = Catalog.objects.all()
    paginator = Paginator(catalog_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        catalog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        catalog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        catalog = paginator.page(paginator.num_pages)

    context = { 'page_header': 'Catalog page',
                'catalog_list': catalog_list,
                'catalog': catalog,
               }
    return render(request, 'polls/index.html', context)

def catalog_detail(request, catalog_id):
    catalog_item = get_object_or_404(Catalog, pk=catalog_id)
    context = {
        'page_header': catalog_item.title,
        'catalog_item': catalog_item,
    }
    return render(request, 'polls/detail.html', context)

def results(request, catalog_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % catalog_id)

def vote(request, catalog_id):
    return HttpResponse("You're voting on question %s." % catalog_id)

def ind(request):
    template = loader.get_template('polls/ind.html')

    #rendering the template in HttpResponse
    return HttpResponse(template.render())

#class ind(TemplateView):
#	template_name = 'polls/index.html'
