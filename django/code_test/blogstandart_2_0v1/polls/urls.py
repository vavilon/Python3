from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:catalog_id>/', views.catalog_detail, name='catalog_detail'),
    # ex: /polls/5/results/
    path('<int:catalog_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:catalog_id>/vote/', views.vote, name='vote'),

    path('te', views.ind, name='ind'),
    url(r'^(?P<catalog_id>[\d+]+)$', views.catalog_detail, name='catalog_detail'),
]
