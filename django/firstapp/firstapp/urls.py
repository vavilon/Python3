# coding: utf-8
from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = ('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('article.urls')),

)