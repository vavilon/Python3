from django.shortcuts import render

# Create your views here.
#from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'index.html')

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')



class HomeView(TemplateView):
    template_name = 'inde.html'
