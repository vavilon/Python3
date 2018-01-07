from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse("hello worls")

class HomeView(TemplateView):
	template_name = 'index.html'

class PageView(TemplateView):
    template_name = 'page.html'
