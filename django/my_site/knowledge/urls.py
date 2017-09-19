from django.conf.urls import url

from . import views

app_name = 'knowledge'
urlpatterns = [
    url(r'^$', views.EKnowledgeIndex.as_view(), name='index'),
    url(r'^(?P<section>[\w]+)/$', views.ESectionView.as_view(), name='section'),
    url(r'^(?P<section>[\w]+)/(?P<article_id>[0-9]+)/$', views.EArticleView.as_view(), name='article')
]
