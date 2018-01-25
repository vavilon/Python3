from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.http import HttpResponse
#from django.http import Http404
#from django.shortcuts import get_object_or_404, render
# Create your views here.


def index(request):
    template = loader.get_template('card/index.html')

    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('card/about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('card/contact.html')
    return HttpResponse(template.render())
