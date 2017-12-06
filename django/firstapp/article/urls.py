#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),


                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
                       url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
                       url(r'^page/(\d+)/$', 'article.views.articles'),
                       url(r'^$', 'article.views.articles'),
                       url(r'^category/get/(?P<category_id>\d+)/$', 'article.views.articl_cat'),
                       url(r'^keyword/$', 'article.views.keywords'),
                       url(r'^author/(?P<id>\d+)/$', 'article.views.authors'),
                       url(r'^home/$', 'article.views.home'),
                       )
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)